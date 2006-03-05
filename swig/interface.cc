#include <iostream>
#include <motility.hh>
#include <IupacMotif.hh>
#include <PwmMotif.hh>
#include <EnergyOperator.hh>

#include "interface.hh"

//
// find_iupac: a procedural interface to the OO-oriented IUPAC motif searching
// stuff.
//

motility::MotifMatchList * find_iupac(char * seq, char * motif,
				    unsigned int n_mismatches)
{
  // Construct the necessary objects:
  motility::IupacMotif motif_obj(motif);
  motility::DnaSequence dna_obj(seq);

  // Set the number of allowed mismatches:
  motif_obj.mismatches(n_mismatches);

  // Do the search:
  motility::MotifMatchList matches = motif_obj.find_matches(dna_obj);

  // Return a new copy.
  return matches.copy();
}

//
// find_pwm: a procedural interface to the OO-oriented PWM searching
// stuff.
//

motility::MotifMatchList * find_pwm(char * seq, _DoubleMatrix * matrix,
				    double threshold)
{
  // Construct the necessary objects:
  motility::PwmMotif motif_obj((double (*)[5])matrix->_matrix, matrix->length);
  motility::DnaSequence dna_obj(seq);

  // Set the threshold:
  motif_obj.match_threshold(threshold);

  // Do the search:
  motility::MotifMatchList matches = motif_obj.find_matches(dna_obj);

  // Return a new copy.
  return matches.copy();
}

//
// find_energy: a procedural interface to the OO-oriented energy operator
// searching stuff.
//

motility::MotifMatchList * find_energy(char * seq, _DoubleMatrix * matrix,
				    double threshold)
{
  // Construct the necessary objects:
  motility::EnergyOperator motif_obj((double (*)[5])matrix->_matrix,
				     matrix->length);
  motility::DnaSequence dna_obj(seq);

  // Set the threshold:
  motif_obj.match_minimum(threshold);

  // Do the search:
  motility::MotifMatchList matches = motif_obj.find_matches(dna_obj);

  // Return a new copy.
  return matches.copy();
}

//
// calc_energy
//

double calc_energy(char * seq, _DoubleMatrix * matrix)
{
  // Construct the necessary objects:
  motility::EnergyOperator motif_obj((double (*)[5])matrix->_matrix,
				     matrix->length);
  motility::DnaSequence dna_obj(seq);

  return motif_obj.calc_score(dna_obj, 0);
}
