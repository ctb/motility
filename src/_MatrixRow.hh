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
#ifndef _MATRIX_ROW_HH
#define _MATRIX_ROW_HH

#include <cctype>

namespace motility {
  class _MatrixRow {
  protected:
    double entries[5];
    int ch_index[256];
  public:
    _MatrixRow(double A, double C, double G, double T, double N) {
      entries[0] = A;
      entries[1] = C;
      entries[2] = G;
      entries[3] = T;
      entries[4] = N;

      ch_index[(int)'A'] = 0;
      ch_index[(int)'C'] = 1;
      ch_index[(int)'G'] = 2;
      ch_index[(int)'T'] = 3;
      ch_index[(int)'N'] = 4;
      ch_index[(int)'X'] = 4;
    }

    double value(char ch) const {
      return entries[ch_index[(int)ch]];
    };

    double max_value(bool use_n=false) const {
      double m = entries[0];

      unsigned int upper = 4;
      if (use_n) upper = 5;

      for (unsigned int i = 1; i < upper; i++ ) {
	if (m < entries[i]) {
	  m = entries[i];
	}
      }
      return m;
    }

    double min_value(bool use_n=false) const {
      double m = entries[0];

      unsigned int upper = 4;
      if (use_n) upper = 5;

      for (unsigned int i = 1; i < upper; i++ ) {
	if (m > entries[i]) {
	  m = entries[i];
	}
      }
      return m;
    }
  };
}

#endif // _MATRIX_ROW_HH
