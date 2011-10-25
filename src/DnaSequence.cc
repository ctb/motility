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
#include "DnaSequence.hh"
#include <cctype>
#include <algorithm>

using namespace motility;

//
// Constructor - convert sequence to uppercase & check to see if it's
// a valid DNA sequence.
//

DnaSequence::DnaSequence(std::string s)
{

  // transform to upper case
  transform(s.begin(), s.end(), s.begin(), toupper);

  std::string::size_type pos = s.find_first_not_of("ACGTNX");

  if (pos != std::string::npos) {
    char ch = s[pos];
    char err[100];
    sprintf(err, "error, invalid character '%c' (%d) in sequence.",
	    ch, int(ch));

    throw DnaException(err);
  }
  
  // made it this far: valid DNA sequence.  store.
  _seq = s;
}

static char complement(char ch)
{
  switch(ch) {
  case 'A':
    return 'T';
  case 'T':
    return 'A';
  case 'C':
    return 'G';
  case 'G':
    return 'C';
  case 'N':
  case 'X':
    return 'N';
  }

  std::string message = "unknown character for complement: ";
  message += ch;

  throw motility::exception(message);
}

//
// Build reverse complement.
//

DnaSequence DnaSequence::reverse_complement() const
{
  std::string r(_seq);
  reverse(r.begin(), r.end());	// first build reverse

  // then build complement
  transform(r.begin(), r.end(), r.begin(), complement);

  return DnaSequence(r);
}
