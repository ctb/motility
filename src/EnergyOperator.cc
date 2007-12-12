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
#include "EnergyOperator.hh"

using namespace motility;

//
// normalize the matrix so that the consensus sequence has a weight of 0.0.
//

void EnergyOperator::normalize()
{
  for (unsigned int i = 0; i < _length; i++) {
    _MatrixRow * old = matrix[i];
    matrix[i] = (_MatrixRow*) (void *) 0;

    double min = old->min_value();

    // definitely a cleaner way to do this by overloading the + operator...
    _MatrixRow * n = new _MatrixRow(old->value('A') - min,
				    old->value('C') - min,
				    old->value('G') - min,
				    old->value('T') - min,
				    old->value('N') - min);
    matrix[i] = n;

    delete old;
  }
}

//
// find matches below the minimum threshold.
//

MotifMatchList * EnergyOperator::find_forward_matches(const DnaSequence& seq) const
{
  MotifMatchList * v = new MotifMatchList();

  for (unsigned int i = 0; i <= seq.length() - _length; i++) {
    double score = calc_score(seq, i);
    if (score <= _minimum) {	// keep it.
      v->add(new MotifMatch(_offset + i, _offset + i + _length,
			    DnaSequence(seq, i, i + _length)));
    }
  }

  return v;
}
