#include <assert.h>
#include "DnaSequence.hh"
#include "MotifMatch.hh"
#include "EnergyOperator.hh"

#include <stdio.h>  /* file needed for io */
#include <iostream>
#include <stdlib.h>

using namespace motility;

int main(int argc, char * argv[])
{
  DnaSequence s("ATAT");

  double matrix[][5] = { { 0.2, 1.0, 1.0, 1.0, 1.0 } }; // 'A'
  EnergyOperator m(matrix, 1);

  printf("minimum score is %.2f before normalization\n", m.min_score());
  m.normalize();
  printf("minimum score is %.2f after normalization\n", m.min_score());

  MotifMatchList l = *m.find_matches(s);
  std::vector<MotifMatch*> l2 = l.list();

  for (unsigned int i = 0; i < l2.size(); i++) {
    MotifMatch * match = l2[i];
    printf("found match: %d --> %d (%s)\n", match->start, match->end,
	   match->match_seq.sequence().c_str());
  }

  double matrix2[][5] = { { 0.2, 1.0, 1.0, 1.0, 1.0 },
			 { 0.2, 1.0, 1.0, 1.0, 1.0 } };

  EnergyOperator m2(matrix2, 2);

  assert(m2.weight_sites_under(0.4, .25, .25) == .25*.25);
  assert(m2.weight_sites_under(1.0, .25, .25) == .25*.25);

  //std::vector<std::string> l3 = m2.generate_sites_under(1.2);
  //for (unsigned int i = 0; i < l3.size(); i++) {
  //printf("%s\n", l3[i].c_str());
  //}
  assert(m2.weight_sites_under(1.2, .25, .25) == (0.25 + 0.25*0.75));
  assert(m2.weight_sites_under(2.0, .25, .25) == 1.0);

  printf("%f\n", m2.weight_sites_under(0.4, .75/2., .25/2.));
  

  exit(0);
}
