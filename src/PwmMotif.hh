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
// Interface for Position-weight matrices.

#ifndef PWM_MOTIF_HH
#define PWM_MOTIF_HH

#include "Motif.hh"
#include "_MatrixMotif.hh"

namespace motility {
  class PwmMotif : public _MatrixMotif {
  protected:
    double _threshold;

    PwmMotif(unsigned int l) : _MatrixMotif(l) { };
  public:
    PwmMotif(double m[][5], unsigned int l) : _MatrixMotif(m, l) {
      _threshold = max_score(); // default to strictest (literal) signifance.
    }

    virtual MotifMatchList find_forward_matches(const DnaSequence& seq) const;

    double match_threshold() const { return _threshold; }
    void match_threshold(double m) { _threshold = m; }
  };
}

#endif // PWM_MOTIF_HH
