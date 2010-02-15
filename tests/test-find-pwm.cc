#include "DnaSequence.hh"
#include "MotifMatch.hh"
#include "PwmMotif.hh"

#include <iostream>
#include <stdlib.h>

using namespace motility;

int main(int argc, char * argv[])
{
  DnaSequence s("ATAT");

  double pwm[][5] = { { 1.0, 0.0, 0.0, 0.0, 0.0, } }; // 'A'
  PwmMotif m(pwm, 1);

  MotifMatchList l = *m.find_matches(s);
  std::vector<MotifMatch*> l2 = l.list();

  for (unsigned int i = 0; i < l2.size(); i++) {
    MotifMatch * match = l2[i];
    printf("found match: %d --> %d (%s)\n", match->start, match->end,
	   match->match_seq.sequence().c_str());
  }

  double pwm2[][5] = { { 1.0, 0.0, 0.0, 0.0, 0.0, },
		      { 1.0, 0.0, 0.0, 0.0, 0.0, },
		      { 1.0, 0.0, 0.0, 0.0, 0.0, },
		      { 1.0, 0.0, 0.0, 0.0, 0.0, }
  }; // 'A'
  PwmMotif m2(pwm2, 4);

  m2.generate_sites_over(0.0);
  m2.generate_sites_under(1.0);

  exit(0);
}
