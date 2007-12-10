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
// Interface for literal motif finding (equiv. exact motif finding).

#ifndef LITERAL_MOTIF_HH
#define LITERAL_MOTIF_HH

#include <string>

#include "Motif.hh"
#include "DnaSequence.hh"
#include "MotifMatch.hh"

namespace motility {
  class LiteralMotif : public Motif {
  protected:
    const std::string _motif;
  public:
    // constructor: checks for validity of sequence as strict DNA
    LiteralMotif(std::string s) : _motif(DnaSequence(s).sequence()) { }

    // constructor: no validity check on DnaSequence.
    LiteralMotif(DnaSequence s) : _motif(s.sequence()) { }

    // find all matches, or just forward / just reverse.
    MotifMatchList find_matches(const DnaSequence& seq) const;
    MotifMatchList find_forward_matches(const DnaSequence& seq) const;
    MotifMatchList find_reverse_matches(const DnaSequence& seq) const;
  };
}

#endif // LITERAL_MOTIF_HH
