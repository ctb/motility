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
#include <stdio.h>   /* required for prt file io */
#include "IupacMotif.hh"
#include <cctype>
#include <algorithm>

using namespace motility;

struct iupac_ids {
  char ch;
  double m[5];
};

static struct iupac_ids _trans_table[] = {
  // simple
  { 'A', { 1.0, 0.0, 0.0, 0.0, 0.0 } },
  { 'C', { 0.0, 1.0, 0.0, 0.0, 0.0 } },
  { 'G', { 0.0, 0.0, 1.0, 0.0, 0.0 } },
  { 'T', { 0.0, 0.0, 0.0, 1.0, 0.0 } },
  { 'N', { 1.0, 1.0, 1.0, 1.0, 1.0 } },

  { 'R', { 1.0, 0.0, 1.0, 0.0, 0.0 } },
  { 'Y', { 0.0, 1.0, 0.0, 1.0, 0.0 } },
  { 'K', { 0.0, 0.0, 1.0, 1.0, 0.0 } },
  { 'M', { 1.0, 1.0, 0.0, 0.0, 0.0 } },
  { 'S', { 0.0, 1.0, 1.0, 0.0, 0.0 } },
  { 'W', { 1.0, 0.0, 0.0, 1.0, 0.0 } },
  { 'B', { 0.0, 1.0, 1.0, 1.0, 0.0 } },
  { 'D', { 1.0, 0.0, 1.0, 1.0, 0.0 } },
  { 'H', { 1.0, 1.0, 0.0, 1.0, 0.0 } },
  { 'V', { 1.0, 1.0, 1.0, 0.0, 0.0 } },
  { 0, { 0.0 } }
};

IupacMotif::IupacMotif(std::string iupac_seq) : PwmMotif(iupac_seq.length())
{
  unsigned int i;

  // transform to upper case
  transform(iupac_seq.begin(), iupac_seq.end(), iupac_seq.begin(), toupper);

  matrix = new _MatrixRow*[_length];
  for (i = 0; i < _length; i++) {
    matrix[i] = NULL;		// in case we throw an exception; see destruct.
  }

  for (unsigned int i = 0; i < _length; i++) {
    bool found = false;
    char ch = iupac_seq[i];
    unsigned int j;

    // first find the element
    for (j = 0; _trans_table[j].ch != 0; j++) {
      if (ch == _trans_table[j].ch) {
	found = true;
	break;
      }
    }

    // make sure we found it
    if (!found) {
      char s[100];
      sprintf(s, "error, invalid character '%c' (%d) for IUPAC motif.",
	    ch, int(ch));

      throw exception(s);
    }

    double * row = &(_trans_table[j].m[0]);
    
    // pwm has already been initialized; now we just need to set the rows:
    matrix[i] = new _MatrixRow(row[0], row[1], row[2], row[3], row[4]);
  }

  mismatches(0);		// set mismatches to 0.

  if (_check_palindromic()) {
    set_palindromic(true);
  } else {
    set_palindromic(false);
  }
}
