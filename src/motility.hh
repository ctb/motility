/*
 * This file is part of the motility source distribution.
 *
 * motility is part of the Cartwheel bioinformatics toolkit:
 *
 *                  http://cartwheel.caltech.edu/
 *
 * Contact author: C. Titus Brown, titus@caltech.edu.
 *
 * This program and all associated source code files are Copyright (C) 2003
 * the California Institute of Technology, Pasadena, CA, 91125 USA.  It is
 * under the Lesser GNU Public License; please see the included LICENSE.txt
 * file for more information, or contact Titus directly.
 *
 */ 
#ifndef MOTILITY_HH
#define MOTILITY_HH

#define MOTILITY_VERSION "0.8.1"

#include <string>

namespace motility {
  // exceptions
  class exception {
  public:
    const std::string msg;

    exception() : msg("") { };
    exception(std::string s) : msg(s) { };
  };
}

#endif // MOTILITY_HH
