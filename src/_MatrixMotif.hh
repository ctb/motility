/*
 * This file is part of the motility source distribution.
 *
 * motility is part of the Cartwheel bioinformatics toolkit:
 *
 *                  http://cartwheel.caltech.edu/
 *
 * Contact author: C. Titus Brown, titus@caltech.edu.
 *
 * This program and all associated source code files are Copyright (C) 2003
 * the California Institute of Technology, Pasadena, CA, 91125 USA.  It is
 * under the Lesser GNU Public License; please see the included LICENSE.txt
 * file for more information, or contact Titus directly.
 *
 */ 

// Interface & base class for motifs based on matrices of doubles (PWM
// or energy operators).  This class provides the majority of the
// functionality: essentially anything that's in common between all
// fixed-size matrix manipulation.
//
// This includes (but isn't limited to) instantiation, 

#ifndef _MATRIX_MOTIF_HH
#define _MATRIX_MOTIF_HH

#include "Motif.hh"
#include "_MatrixRow.hh"
#include <string>
#include <vector>

namespace motility {

  //
  // _MatrixMotif
  //

  class _MatrixMotif : public Motif {
  protected:
    // the actual matrix.
    _MatrixRow ** matrix;

    // the size of the matrix.
    const unsigned int _length;

    // constructor: create an empty matrix of the given length.
    _MatrixMotif(unsigned int l) : _length(l) {
      if (l == 0) {
	throw motility::exception("length must be greater than 0.");
      }

      matrix = NULL;
    }

    // constructor: load the matrix in from the passed-in double[][5].
    _MatrixMotif(double m[][5], unsigned int l) : _length(l) {
      if (l == 0) {
	throw motility::exception("length must be greater than 0.");
      }

      matrix = new _MatrixRow*[_length];

      for (unsigned int i = 0; i < _length; i++) {
	matrix[i] = new _MatrixRow(m[i][0], m[i][1], m[i][2],
				   m[i][3], m[i][4]);
      }

      // Check to see if the site picked out by this matrix is palindromic.
      //
      // (Damn you, Chris Hart!)

      if (_check_palindromic()) {
	_is_palindromic = true;
      } else {
	_is_palindromic = false;
      }
    }

    bool _is_palindromic;
    const bool _check_palindromic() const;

    void set_palindromic(bool v) { _is_palindromic = v; }

    // recursive work functions for generate_sites_over/generate_sites_under.

    void _r_generate_sites_over(const double min_score,
				const double cur_score,
				const unsigned int pos,
				const std::string sofar,
				std::vector<std::string> &l,
				const bool use_n=false) const;

    void _r_generate_sites_under(const double max_score,
				 const double cur_score,
				 const unsigned int pos,
				 const std::string sofar,
				 std::vector<std::string> &l,
				 const bool use_n=false) const;

    double _r_weight_sites_over(const double min_score,
				const double cur_score,
				const unsigned int pos,
				const double sofar,
				const double AT_bias,
				const double GC_bias) const;

    double _r_weight_sites_under(const double max_score,
				 const double cur_score,
				 const unsigned int pos,
				 const double sofar,
				 const double AT_bias,
				 const double GC_bias) const;
  public:

    // destructor: deallocate matrix.
    virtual ~_MatrixMotif() {
      if (matrix) {
	for (unsigned int i = 0; i < _length; i++) {
	  if (matrix[i]) { delete matrix[i]; }
	}
	delete matrix;
      }
    }

    // get the length.
    const unsigned int length() const { return _length; }

    // Do forward+rc, forward-only, or rc-only searching.
    // Note that find_matches and find_reverse_matches are implemented using
    // find_forward_matches.
    
    MotifMatchList find_matches(const DnaSequence& seq) const;
    virtual MotifMatchList find_forward_matches(const DnaSequence& seq) const
      = 0;
    MotifMatchList find_reverse_matches(const DnaSequence& seq) const;

    // Calculate the min/max score.
    const double max_score(bool use_n=false) const;
    const double min_score() const;

    // calculate the score of a specific sequence.
    virtual double calc_score(const DnaSequence& seq, unsigned int pos) const;

    // check to see if it's a palindromic matrix.
    const bool is_palindromic() const { return _is_palindromic; };

    // Calculate the sequence of all of the motifs with a score
    // above/below the given threshold.
    //
    // (potentially VERY time consuming...)

    std::vector<std::string> generate_sites_over(double min_score,
						 bool use_n=false) const;
    std::vector<std::string> generate_sites_under(double max_score,
						  bool use_n=false) const;

    double weight_sites_over(double min_score,
			     const double AT_bias, const double GC_bias)
      const;
    double weight_sites_under(double max_score,
			      const double AT_bias, const double GC_bias)
      const;
			     
  };
}

#endif // _MATRIX_MOTIF_HH
