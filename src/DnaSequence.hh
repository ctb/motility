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
#ifndef DNA_SEQUENCE_HH
#define DNA_SEQUENCE_HH

#include <string>

#include "motility.hh"

namespace motility {
  class DnaException : public exception {
  public:
    DnaException(std::string s) : exception(s) { };
  };

  class DnaSequence {
  protected:
    std::string _seq;
  public:
    DnaSequence() { };		// do nothing.

    // general constructor: build a DnaSequence from a string. checks validity.
    DnaSequence(std::string s);

    // build a DnaSequence from a substring of another DnaSequence.
    // no validity check.
    DnaSequence(const DnaSequence& s, unsigned int a, unsigned int b) :
      _seq(s._seq.substr(a, b-a)) {
      if (b - a <= 0) throw exception("invalid start/end coordinates.");
    };

    // return sequence as string.
    const std::string sequence() const { return _seq; }

    // return length
    const unsigned int length() const { return _seq.length(); }

    DnaSequence reverse_complement() const; // build reverse complement

    bool is_palindrome() const { return (reverse_complement()._seq == _seq); };
  };
}

#endif // DNA_SEQUENCE_HH
