#include <vector>
#include <MotifMatch.hh>

typedef struct {
  double *_matrix;
  unsigned int length;
} _DoubleMatrix;

motility::MotifMatchList * find_iupac(char * seq, char * motif,
				      unsigned int n_mismatches);

motility::MotifMatchList * find_pwm(char * seq, _DoubleMatrix * matrix,
				    double threshold);

motility::MotifMatchList * find_energy(char * seq, _DoubleMatrix * matrix,
				       double threshold);

double calc_energy(char * seq, _DoubleMatrix * matrix);
