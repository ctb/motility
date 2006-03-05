"""
Base Python objects for motif searching: position-weight matrix/energy
operators, and an IUPAC searching implementation done with PWMs.
"""

import _motility

#
# EnergyOperator
#

class EnergyOperator:
    """
    Energy operator class.
    """
    def __init__(self, m, default_n_value=1000):
        """
        Constructor.  Takes a 4- or 5-by-N array representing the scores
        for [A,C,G,T[,N]].  The optional 'default_n_value' argument gives
        the default value for 'N' matches.
        """
        self.matrix = m
        self._m = _motility.create_matrix(m, default_n_value)

    def __len__(self):
        """
        Returns the length of the sites that will be scored.
        """
        return len(self._m)

    def find(self, seq, threshold):
        """
        Search the given sequence for matches with scores
        less than or equal to the given threshold.
        """
        return _motility.find_energy(seq, self._m, threshold)

    def calc_energy(self, motif):
        """
        Calculate the score for the given site.  'motif' must be of the
        same length as the operator.
        """
        return _motility.calc_energy(motif, self._m)

    def min_score(self, use_n=0):
        """
        Calculate the best (minimum) possible score for this operator.  By
        default, do not count 'N' scores.
        """
        return _motility.min_score(self._m, use_n)

    def max_score(self, use_n=0):
        """
        Calculate the worst (maximum) possible score for this operator. By
        default, do not count 'N' scores.
        """
        return _motility.max_score(self._m, use_n)

    def generate_sites_under(self, threshold, use_n=0):
        """
        Generate a list of all sites under this threshold.
        """
        return _motility.generate_sites_under(self._m, threshold, use_n)

    def weight_sites_under(self, threshold, AT_bias=.25, GC_bias=.25):
        """
        Calculate the combined weight of all sites under this threshold,
        using the given AT/GC biases.
        """
        return _motility.weight_sites_under(self._m, threshold,
                                            AT_bias, GC_bias)
    
#
# PWM
#

class PWM:
    """
    Position Weight Matrix class.
    """
    def __init__(self, m, default_n_value=-1000):
        """
        Constructor.  Takes a 4- or 5-by-N array representing the scores
        for [A,C,G,T[,N]].
        """
        self.matrix = m
        self._m = _motility.create_matrix(m, default_n_value)

    def __len__(self):
        """
        Returns the length of the sites that will be scored.
        """
        return len(self._m)

    def find(self, seq, threshold):
        """
        Search the given sequence for matches with scores less than or
        equal to the given threshold.
        """
        return _motility.find_pwm(seq, self._m, threshold)

    def calc_score(self, motif):
        """
        Calculate the score for the given site.  'motif' must be of the
        same length as the PWM.
        """
        return _motility.calc_score(motif, self._m)

    def min_score(self, use_n=0):
        """
        Calculate the worst (minimum) possible score for this operator.
        By default, do not count 'N' scores.
        """
        return _motility.min_score(self._m, use_n)

    def max_score(self, use_n=0):
        """
        Calculate the worst (maximum) possible score for this operator.
        By default, do not count 'N' scores.
        """
        return _motility.max_score(self._m, use_n)

    def generate_sites_over(self, threshold, use_n=0):
        """
        Generate a list of all sites under this threshold.
        """
        return _motility.generate_sites_over(self._m, threshold, use_n)

    def weight_sites_over(self, threshold, AT_bias=.25, GC_bias=.25):
        """
        Calculate the combined weight of all sites under this threshold,
        using the given AT/GC biases.
        """
        return _motility.weight_sites_over(self._m, threshold,
                                           AT_bias, GC_bias)

iupac_translate = \
  { 'A' : [ 1.0, 0.0, 0.0, 0.0, 0.0, ],
    'C' : [ 0.0, 1.0, 0.0, 0.0, 0.0, ],
    'G' : [ 0.0, 0.0, 1.0, 0.0, 0.0, ],
    'T' : [ 0.0, 0.0, 0.0, 1.0, 0.0, ],
    'N' : [ 1.0, 1.0, 1.0, 1.0, 1.0, ],
    'R' : [ 1.0, 0.0, 1.0, 0.0, 0.0, ],
    'Y' : [ 0.0, 1.0, 0.0, 1.0, 0.0, ],
    'K' : [ 0.0, 0.0, 1.0, 1.0, 0.0, ],
    'M' : [ 1.0, 1.0, 0.0, 0.0, 0.0, ],
    'S' : [ 0.0, 1.0, 1.0, 0.0, 0.0, ],
    'W' : [ 1.0, 0.0, 0.0, 1.0, 0.0, ],
    'B' : [ 0.0, 1.0, 1.0, 1.0, 0.0, ],
    'D' : [ 1.0, 0.0, 1.0, 1.0, 0.0, ],
    'H' : [ 1.0, 1.0, 0.0, 1.0, 0.0, ],
    'V' : [ 1.0, 1.0, 1.0, 0.0, 0.0, ] }


class IUPAC(PWM):
    """
    IUPAC searching via a PWM.
    """
    def __init__(self, motif):
        """
        Constructor.  Build a PWM from an IUPAC string.
        """
        self.motif = motif

        matrix = []
        for ch in self.motif:
            l = iupac_translate[ch]
            matrix.append(l)
            
        PWM.__init__(self, matrix)

    def find(self, seq, threshold=None):
        """
        Search the given sequence for matches with scores less than or
        equal to the given threshold.  If no threshold given, assume
        exact match to IUPAC motif.
        """
        if threshold is None:
            threshold = len(self)
        return _motility.find_pwm(seq, self._m, threshold)

    def find_with_mismatches(self, seq, mismatches=0):
        """
        Search for matches to an IUPAC string, but allow mismatches.
        """
        if mismatches >= len(self.motif):
            raise Exception("error, more mismatches than bases in motif!")
            
        return self.find(seq, len(self.motif) - mismatches)
