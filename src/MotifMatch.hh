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
#ifndef MOTIF_MATCH_HH
#define MOTIF_MATCH_HH

#include "DnaSequence.hh"
#include <assert.h>
#include <vector>

namespace motility {
  class MotifMatch {
  public:
    const unsigned int start, end;
    const DnaSequence match_seq;

    MotifMatch(unsigned int s, unsigned int e, DnaSequence m) :
      start(s), end(e), match_seq(m) { };

    MotifMatch * copy() const { return new MotifMatch(start, end, match_seq); }
  };

  class MotifMatchList {
  protected:
    std::vector<MotifMatch*> l;
  public:
    MotifMatchList() { };
    MotifMatchList(std::vector<MotifMatch*> n) { l = n; } // inefficient

    // make a copy of this list
    MotifMatchList * copy() const {
      std::vector<MotifMatch*> n;
      for (unsigned int i = 0; i < l.size(); i++) {
	n.push_back(l[i]->copy());
      }
      return new MotifMatchList(n);
    }

    // Add an element to the vector
    void add(MotifMatch* m) { l.push_back(m); }

    // get the list of elements.
    std::vector<MotifMatch*> list() { return l; }

    unsigned int size() const { return l.size(); }

    // Clean up the motif matches.
    virtual ~MotifMatchList() {
      for (unsigned int i = 0; i < l.size(); i++) {
	delete l[i];
      }
    }
  };
}

#endif // MOTIF_MATCH_HH
