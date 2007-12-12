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
// Implementation of literal (== exact) motif finding.

#include "LiteralMotif.hh"

using namespace motility;

//
// find all matches, both forward and reverse complement.
//

MotifMatchList * LiteralMotif::find_matches(const DnaSequence& seq) const
{
  MotifMatchList * v = find_forward_matches(seq);

  DnaSequence m(_motif);
  if (!m.is_palindrome()) {
    MotifMatchList * r = find_reverse_matches(seq);
    std::vector<MotifMatch *> l = r->list();
    for (unsigned int i = 0; i < l.size(); i++) {
      MotifMatch * m = l[i];
      v->add(new MotifMatch(m->start, m->end, m->match_seq));
    }
  }

  return v;
}

//
// find only forward matches.
//

MotifMatchList * LiteralMotif::find_forward_matches(const DnaSequence& seq) const
{
  printf("OFFSET IS: %d\n", _offset);
  MotifMatchList * v = new MotifMatchList();
  const unsigned int length = _motif.length();

  std::string dna = seq.sequence();
  std::string::size_type pos;

  pos = dna.find(_motif);
  while (pos != std::string::npos) {
    
    v->add(new MotifMatch(_offset + pos, _offset + pos + length,
			  dna.substr(pos, length)));
    printf("pos: %d\n", _offset + pos);
			   
    pos = dna.find(_motif, pos + 1);
  } 

  return v;
}

//
// find only reverse matches.
//

MotifMatchList * LiteralMotif::find_reverse_matches(const DnaSequence& seq)
  const
{
  DnaSequence rc = seq.reverse_complement();
  MotifMatchList * v = find_forward_matches(rc);

  std::vector<MotifMatch*> l = v->list();
  unsigned int length = seq.length();

  MotifMatchList * r = new MotifMatchList();
  for (unsigned int i = 0; i < l.size(); i++) {
    const MotifMatch * m = l[i];
    unsigned int new_start, new_end;
    new_start = length - m->start + 2*_offset;
    new_end = length - m->end + 2*_offset;

    // reverse match & sequence, then add.  kinda clumsy ;(.

    r->add(new MotifMatch(new_start, new_end,
			  m->match_seq.reverse_complement()));
  }

  delete v;

  return r;
}
