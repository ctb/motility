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
// Interface for energy operator-style motifs.

#ifndef ENERGY_OPERATOR_HH
#define ENERGY_OPERATOR_HH

#include "Motif.hh"
#include "_MatrixMotif.hh"

namespace motility {
  class EnergyOperator : public _MatrixMotif {
  protected:
    EnergyOperator(unsigned int l) : _MatrixMotif(l) { };
    double _minimum;
  public:
    EnergyOperator(double m[][5], unsigned int l) : _MatrixMotif(m, l) {
      _minimum = min_score(); // default to strictest (literal) signif.
    }

    virtual MotifMatchList * find_forward_matches(const DnaSequence& seq) const;
    
    // normalize so that the consensus sequence has a weight of 0.0.
    void normalize();

    double match_minimum() const { return _minimum; }
    void match_minimum(double m) { _minimum = m; }
  };
}

#endif // ENERGY_OPERATOR_HH
