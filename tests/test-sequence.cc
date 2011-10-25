#include "DnaSequence.hh"
#include "_MatrixRow.hh"
#include "PwmMotif.hh"

#include <stdio.h> /* file needed for io */
#include <iostream>
#include <stdlib.h>

using namespace motility;

int main(int argc, char * argv[])
{
  DnaSequence s("ATCGN");
  
  if (s.sequence() != s.reverse_complement().reverse_complement().sequence()) {
    printf("Error! RC of RC doesn't match original.\n");
    exit(-1);
  }
  
  bool was_err = false;
  try {
    DnaSequence err("ATCGNB");
  } catch(const motility::exception& exc) {
    was_err = true;
  }

  if (!was_err) { printf("Error! Bad sequence accepted.\n"); exit(-1); }

  exit(0);
}
