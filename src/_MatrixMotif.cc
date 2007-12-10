/*
 * This file is part of the motility source distribution.
 *
 * motility is part of the Cartwheel bioinformatics toolkit:
 *
 *                  http://cartwheel.caltech.edu/
 *
 * Contact author: C. Titus Brown, titus@caltech.edu.
 *
 * This program and all associated source code files are Copyright (C)
 * 2003-2007 the California Institute of Technology, Pasadena, CA,
 * 91125 USA.  It is under the Lesser GNU Public License; please see
 * the included LICENSE.txt file for more information, or contact
 * Titus directly.
 *
 */ 
#include "_MatrixMotif.hh"

using namespace motility;

const double _MatrixMotif::max_score(bool use_n) const
{
  double total = 0.;

  for (unsigned int i = 0; i < _length; i++) {
    _MatrixRow * r = matrix[i];
    total += r->max_value(use_n);
  }
  return total;
}

const double _MatrixMotif::min_score(bool use_n) const
{
  double total = 0.;

  for (unsigned int i = 0; i < _length; i++) {
    _MatrixRow * r = matrix[i];
    total += r->min_value(use_n);
  }
  return total;
}

//
// the workhorse function: run through the matrix and calculate the
// actual match.
//

double _MatrixMotif::calc_score(const DnaSequence& seq, unsigned int pos) const
{
  if (pos + _length > seq.length()) {
    throw exception("motif to score extends beyond end of sequence");
  }

  double total = 0.;
  std::string sequence = seq.sequence();
  const char * cptr = sequence.c_str() + pos;

  for (unsigned int i = 0; i < _length; i++) {
    total += matrix[i]->value(cptr[i]);
  }
  return total;
}

MotifMatchList _MatrixMotif::find_matches(const DnaSequence& seq) const
{
  MotifMatchList v = find_forward_matches(seq);

  if (!is_palindromic()) {
    MotifMatchList r = find_reverse_matches(seq);

    std::vector<MotifMatch *> l = r.list();
    for (unsigned int i = 0; i < l.size(); i++) {
      MotifMatch * m = l[i];
      v.add(new MotifMatch(m->start, m->end, m->match_seq));
    }
  }

  return v;
}

MotifMatchList _MatrixMotif::find_reverse_matches(const DnaSequence& seq) const
{
  DnaSequence rc = seq.reverse_complement();
  MotifMatchList v = find_forward_matches(rc);

  std::vector<MotifMatch*> l = v.list();
  unsigned int length = seq.length();

  MotifMatchList r;
  for (unsigned int i = 0; i < l.size(); i++) {
    const MotifMatch * m = l[i];
    unsigned int new_start, new_end;
    new_start = length - m->start;
    new_end = length - m->end;

    // reverse match & sequence, then add.  kinda clumsy ;(.

    r.add(new MotifMatch(new_start, new_end,
			 m->match_seq.reverse_complement()));
  }

  return r;
}

//
// _check_palindromic()
//

const bool _MatrixMotif::_check_palindromic() const
{
  unsigned int i;

  for (i = 0; i < _length / 2; i++) {
    int front = i;
    int back = _length - front - 1;
    
    if (matrix[front]->value('A') == matrix[back]->value('T') &&
	matrix[front]->value('C') == matrix[back]->value('G') &&
	matrix[front]->value('G') == matrix[back]->value('C') &&
	matrix[front]->value('T') == matrix[back]->value('A') &&
	matrix[front]->value('N') == matrix[back]->value('N')) {
      ;
    } else {
      return false;
    }
  }

  // odd length?
  if (_length % 2 == 1) {
    int mid = _length / 2;
    if (matrix[mid]->value('A') == matrix[mid]->value('T') &&
	matrix[mid]->value('G') == matrix[mid]->value('C')) {
      ;
    } else {
      return false;
    }
  }

  return true;
}

std::vector<std::string> _MatrixMotif::generate_sites_over(double _min_score,
							   bool use_n) const
{
  std::vector<std::string> l;

  // start with max_score()
  _r_generate_sites_over(_min_score, max_score(), 0, "", l);

  return l;
}

std::vector<std::string> _MatrixMotif::generate_sites_under(double _max_score,
							    bool use_n) const
{
  std::vector<std::string> l;

  // start with 0.0
  _r_generate_sites_under(_max_score, 0.0, 0, "", l);
  
  return l;
}

void _MatrixMotif::_r_generate_sites_over(const double min_score,
					  const double cur_score,
					  const unsigned int pos,
					  const std::string sofar,
					  std::vector<std::string> &l,
					  const bool use_n) const
{
  if (cur_score < min_score) {
    return;
  }

  if (pos == _length) {
    l.push_back(sofar);
    return;
  }

  double max_val = matrix[pos]->max_value(use_n);

  char ch;

  ch = 'A';
  _r_generate_sites_over(min_score,
			 cur_score - (max_val - matrix[pos]->value(ch)),
			 pos + 1, sofar + ch, l, use_n);

  ch = 'C';
  _r_generate_sites_over(min_score,
			 cur_score - (max_val - matrix[pos]->value(ch)),
			 pos + 1, sofar + ch, l, use_n);

  ch = 'G';
  _r_generate_sites_over(min_score,
			 cur_score - (max_val - matrix[pos]->value(ch)),
			 pos + 1, sofar + ch, l, use_n);

  ch = 'T';
  _r_generate_sites_over(min_score,
			 cur_score - (max_val - matrix[pos]->value(ch)),
			 pos + 1, sofar + ch, l, use_n);

  if (use_n) {
    ch = 'N';
    _r_generate_sites_over(min_score,
			   cur_score - (max_val - matrix[pos]->value(ch)),
			   pos + 1, sofar + ch, l, use_n);
  }
}

void _MatrixMotif::_r_generate_sites_under(const double max_score,
					   const double cur_score,
					   const unsigned int pos,
					   const std::string sofar,
					   std::vector<std::string> &l,
					   const bool use_n) const
{
  if (cur_score > max_score) {
    return;
  }

  if (pos == _length) {
    l.push_back(sofar);
    return;
  }

  char ch;

  ch = 'A';
  _r_generate_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			  pos + 1, sofar + ch, l, use_n);

  ch = 'C';
  _r_generate_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			  pos + 1, sofar + ch, l, use_n);

  ch = 'G';
  _r_generate_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			  pos + 1, sofar + ch, l, use_n);

  ch = 'T';
  _r_generate_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			  pos + 1, sofar + ch, l, use_n);

  if (use_n) {
    ch = 'N';
    _r_generate_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			    pos + 1, sofar + ch, l, use_n);
  }

}

double _MatrixMotif::weight_sites_under(double _max_score,
					const double AT_bias,
					const double GC_bias) const
{
  //  if (2*AT_bias + 2*GC_bias != 1.0) {
  //    throw motility::exception("AT_bias + GC_bias must equal 0.5!");
  //}

  // start with 0.0
  return _r_weight_sites_under(_max_score, 0.0, 0, 1.0, AT_bias, GC_bias);
}

double _MatrixMotif::_r_weight_sites_under(const double max_score,
					   const double cur_score,
					   const unsigned int pos,
					   const double sofar,
					   const double AT_bias,
					   const double GC_bias) const
{
  double ret = 0.0;

  if (cur_score > max_score) {
    return 0.;
  }

  if (pos == _length) {
    return sofar;
  }

  char ch;

  // use AT bias

  ch = 'A';
  ret += _r_weight_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			       pos + 1, sofar * AT_bias, AT_bias, GC_bias);
  ch = 'T';
  ret += _r_weight_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			       pos + 1, sofar * AT_bias, AT_bias, GC_bias);

  // switch to GC bias

  ch = 'G';
  ret += _r_weight_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			       pos + 1, sofar * GC_bias, AT_bias, GC_bias);

  ch = 'C';
  ret += _r_weight_sites_under(max_score, cur_score + matrix[pos]->value(ch),
			       pos + 1, sofar * GC_bias, AT_bias, GC_bias);

  return ret;
}


double _MatrixMotif::weight_sites_over(double _min_score,
				       const double AT_bias,
				       const double GC_bias) const
{
  //if (2*AT_bias + 2*GC_bias != 1.0) {
  //throw motility::exception("AT_bias + GC_bias must equal 0.5!");
  //}

  // start with 0.0
  return _r_weight_sites_over(_min_score, max_score(), 0, 1.0,
			       AT_bias, GC_bias);
}

double _MatrixMotif::_r_weight_sites_over(const double min_score,
					  const double cur_score,
					  const unsigned int pos,
					  const double sofar,
					  const double AT_bias,
					  const double GC_bias) const
{
  double ret = 0.0;

  if (cur_score < min_score) {
    return 0.;
  }

  if (pos == _length) {
    return sofar;
  }

  double max_val = matrix[pos]->max_value(false);

  char ch;

  // use AT bias

  ch = 'A';
  ret += _r_weight_sites_over(min_score,
			      cur_score - (max_val - matrix[pos]->value(ch)),
			      pos + 1, sofar * AT_bias, AT_bias, GC_bias);

  ch = 'T';
  ret += _r_weight_sites_over(min_score,
			      cur_score - (max_val - matrix[pos]->value(ch)),
			      pos + 1, sofar * AT_bias, AT_bias, GC_bias);
  // switch to GC bias

  ch = 'G';
  ret += _r_weight_sites_over(min_score,
			      cur_score - (max_val - matrix[pos]->value(ch)),
			      pos + 1, sofar * GC_bias, AT_bias, GC_bias);

  ch = 'C';
  ret += _r_weight_sites_over(min_score,
			      cur_score - (max_val - matrix[pos]->value(ch)),
			      pos + 1, sofar * GC_bias, AT_bias, GC_bias);

  return ret;
}

