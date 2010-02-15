#include "DnaSequence.hh"
#include "MotifMatch.hh"
#include "LiteralMotif.hh"

#include <iostream>
#include <stdlib.h>

using namespace motility;

int main(int argc, char * argv[])
{
  DnaSequence s("ATAT");
  LiteralMotif m("A");
  MotifMatchList l = *m.find_matches(s);
  std::vector<MotifMatch*> l2 = l.list();

  for (unsigned int i = 0; i < l2.size(); i++) {
    MotifMatch * match = l2[i];
    printf("found match: %d --> %d (%s)\n", match->start, match->end,
	   match->match_seq.sequence().c_str());
  }

  exit(0);
}
