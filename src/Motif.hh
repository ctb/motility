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
#ifndef MOTIF_HH
#define MOTIF_HH

#include "DnaSequence.hh"
#include "MotifMatch.hh"
#include <vector>

namespace motility {
  class Motif {
  protected:
    Motif() : _offset(0) { };
    virtual ~Motif() { };
    unsigned int _offset;
  public:

    void offset(int o) {
      _offset = o;
    }

    virtual MotifMatchList * find_matches(const DnaSequence& seq) const = 0;
    virtual MotifMatchList * find_forward_matches(const DnaSequence& seq) const
      = 0;
    virtual MotifMatchList * find_reverse_matches(const DnaSequence& seq) const
      = 0;
  };
}

# endif // MOTIF_HH
