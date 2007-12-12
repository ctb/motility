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
// Interface for IUPAC motif finding.

#ifndef IUPAC_MOTIF_HH
#define IUPAC_MOTIF_HH

#include "PwmMotif.hh"

namespace motility {
  class IupacMotif : protected PwmMotif { // hide PwmMotif score stuff
  public:
    IupacMotif(std::string s);

    void mismatches(unsigned int n) {
      match_threshold(max_score() - n);
    }
    unsigned int mismatches() const {
      return (unsigned int) (max_score() - match_threshold());
    }
    
    const bool is_palindromic() const { return PwmMotif::is_palindromic(); }

    virtual MotifMatchList * find_matches(const DnaSequence& seq) const {
      return PwmMotif::find_matches(seq);
    }
    virtual MotifMatchList * find_forward_matches(const DnaSequence& seq) const {
      return PwmMotif::find_forward_matches(seq);
    }
    virtual MotifMatchList * find_reverse_matches(const DnaSequence& seq) const {
      return PwmMotif::find_reverse_matches(seq);
    }
  };
}

#endif // IUPAC_MOTIF_HH
