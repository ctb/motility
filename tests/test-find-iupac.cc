#include "DnaSequence.hh"
#include "MotifMatch.hh"
#include "IupacMotif.hh"

#include <iostream>
#include <assert.h>

using namespace motility;

int main(int argc, char * argv[])
{
  DnaSequence s("ATAT");

  IupacMotif m("W");

  MotifMatchList l = *m.find_matches(s);
  std::vector<MotifMatch*> l2 = l.list();

  for (unsigned int i = 0; i < l2.size(); i++) {
    MotifMatch * match = l2[i];
    printf("found match: %d --> %d (%s)\n", match->start, match->end,
	   match->match_seq.sequence().c_str());
  }

  IupacMotif m2("AA");

  printf("found %d matches with %d allowed mismatches.\n",
	 m2.find_matches(s)->size(), m2.mismatches());

  m2.mismatches(1);
  printf("found %d matches with %d allowed mismatch.\n",
	 m2.find_matches(s)->size(), m2.mismatches());

  IupacMotif m3("CG");
  m3.mismatches(1);
  printf("found %d matches with %d allowed mismatch.\n",
	 m3.find_matches(s)->size(), m3.mismatches());

  m3.mismatches(2);
  printf("found %d matches with %d allowed mismatches.\n",
	 m3.find_matches(s)->size(), m3.mismatches());

  IupacMotif m4("ATA");
  printf("found %d matches with %d allowed mismatches.\n",
	 m4.find_matches(s)->size(), m4.mismatches());

  std::string str("ATGGC");
  for (unsigned int i = 0; i < 80000; i++) {
    str += "ATGGC";
  }
  printf("str is now len %d\n", (int) str.length());

  DnaSequence g(str);
  IupacMotif m5("ATTGGCATTG");
  printf("searching...");
  fflush(stdout);
  m5.find_matches(g);

  IupacMotif m6("ATCGNCGAT");
  assert(m6.is_palindromic());

  printf("...done\n");

  exit(0);
}
