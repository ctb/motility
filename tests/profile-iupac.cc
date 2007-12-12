#include "DnaSequence.hh"
#include "MotifMatch.hh"
#include "IupacMotif.hh"

#include <iostream>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

// using namespace motility;

int main(int argc, char * argv[])
{
  FILE * fp;

  printf("hello, world\n");

  fp = fopen("50mb-random.fa", "r");

  char * buf = (char *) malloc(50*1024*1024);
  printf("%x\n", buf);
  int x = fread(buf, 1, 5*1024*1024, fp);

  printf("read %d\n", x);

  buf[x] = 0;

  motility::DnaSequence s(buf);

  motility::IupacMotif m("GATA");

  motility::MotifMatchList l = *m.find_matches(s);
  std::vector<motility::MotifMatch*> l2 = l.list();

  printf("%d\n", l2.size());

  exit(0);
}
