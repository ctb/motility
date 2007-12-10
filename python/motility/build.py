"""
Functions to build motif representations.

Functions in this module:

 * make_iupac_motif(sites) - build an IUPAC motif from a list of sites
 
 * make_matrix(sites, cell_fn, cls=None) - function to build matrix reprs
 
 * make_PWM - make a PWM (Position Weight Matrix)
 
 * make_operator - make an EnergyOperator
 
 * count_bases_by_position(sites) - util function to calculate column info
"""

__all__ = ['count_bases_by_position',
           'make_iupac_motif',
           'make_matrix',
           'make_PWM',
           'make_operator']

import math
from _motility import MotilityError
from objects import iupac_translate, PWM, EnergyOperator

# reverse iupac_translate dictionary
iupac_translate_rev = {}
for (k, v) in iupac_translate.items():
    iupac_translate_rev[tuple(v[:4])] = k

def count_bases_by_position(sites):
    """
    Takes a list of DNA sites and counts how many bases are in each position.

    The return value is a list of dictionaries, with each dictionary containing
    (nucleotide=count) pairs for that position.

    This is mainly of use for constructing position-weight matrices.

    For example,

    >>> count_bases_by_position(['A', 'T', 'C', 'G'])
    [{'A': 1, 'C': 1, 'T': 1, 'G': 1}]

    and
    
    >>> count_bases_by_position(['AA', 'TA', 'CA', 'GA'])
    [{'A': 1, 'C': 1, 'T': 1, 'G': 1}, {'A': 4, 'C': 0, 'T': 0, 'G': 0}]
    """

    # first, check to make sure that all of the input sites are the same
    # length.
    
    sites_len = [len(l) for l in sites]

    if min(sites_len) == 0:
        raise MotilityError("you cannot use length-zero sites")

    if min(sites_len) != max(sites_len):
        raise MotilityError("all input sites must be the same length")
    
    sites_len = min(sites_len)

    #
    # now, for each position, count & compute.
    #

    z = []
    for i in range(0, sites_len):

        # make a string that contains the vertical...
        s = ""
        for j in range(0, len(sites)):
            s += sites[j][i]

        d = dict(A=s.count('A'),
                 T=s.count('T'),
                 C=s.count('C'),
                 G=s.count('G'))

        if not sum(d.values()) == len(s):
            raise MotilityError("input sites are not all DNA: position %d" % i)

        z.append(d)

    return z

def make_iupac_motif(sites):
    """
    Translate a list of DNA sites into an all-inclusive IUPAC motif.

    For example,
    
    >>> make_iupac_motif(['AA', 'TA', 'CA', 'GA'])
    'NA'

    and
    
    >>> make_iupac_motif(['AGATAA', 'TGATAA', 'AGATAG'])
    'WGATAR'
    """
    base_counts = count_bases_by_position(sites)

    def make_binary_choice(x):
        if x:
            return 1.0
        return 0.0

    iupac_site = ""
    for d in base_counts:

        # turn each 4-tuple of base counts into an index into
        # iupac_translate_rev
        
        combo = [make_binary_choice(d[ch]) for ch in 'ACGT']
        combo = tuple(combo)

        iupac_site += (iupac_translate_rev[combo])
        
    return iupac_site

def make_matrix(sites, cell_fn, cls=None):
    """
    A generic function to make matrices from a list of DNA sites.

     - 'sites' is the list of sites

     - 'cell_fn' is a function of three arguments, N_base, max_count, and
       sum_count, where those numbers are calculated over each column.
       cell_fn is used to calculate the entry for each cell.

     - the optional 'cls' argument specifies a class to apply to the resulting
       matrix before returning it, e.g. EnergyOperator or PWM.
    
    >>> cell_fn = lambda x, y, z: float(x) / float(z)
    
    >>> operator = make_matrix(['AA', 'TA', 'CA', 'GA'], cell_fn, PWM)
    >>> operator.calc_score('AA')
    1.25

    >>> operator.calc_score('GT')
    0.25

    >>> cell_fn = lambda x, y, z: float(x) / float(y)
    
    >>> operator = make_matrix(['AA', 'TA', 'CA', 'GA'], cell_fn, PWM)
    >>> operator.calc_score('AA')
    2.0

    >>> operator.calc_score('GT')
    1.0
    """
    base_counts = count_bases_by_position(sites)

    matrix = []
    for d in base_counts:
        column = [d[ch] for ch in 'ACGT']
        max_freq = max(column)
        n_sites = sum(column)
        
        column = [ cell_fn(i, max_freq, n_sites) for i in column ]
        matrix.append(column)

    if cls:
        matrix = cls(matrix)

    return matrix

def make_PWM(sites):
    """
    Make a position-weight matrix from sites, with scores that represent
    frequency of each base.
    
    >>> operator = make_PWM(['AA', 'TA', 'CA', 'GA'])
    >>> operator.calc_score('AA')
    1.25

    >>> operator.calc_score('GT')
    0.25
    """
    # x = base count, z = sum of all counts, x / z = frequency of base
    cell_fn = lambda x, y, z: float(x) / float(z)
    return make_matrix(sites, cell_fn, PWM)

def make_operator(sites):
    """
    Make an "energy operator" from sites, with scores that represent
    binding energy.  Here, lower scores are better.
    
    >>> operator = make_operator(['AA', 'TA', 'CA', 'GA'])
    >>> operator.calc_energy('AA')
    0.0

    >>> operator.calc_energy('GT')
    1.6094379124341003
    """
    # x = base count, y = max count
    cell_fn = lambda x, y, z: math.log((float(y) + 1) / (float(x) + 1))
    return make_matrix(sites, cell_fn, EnergyOperator)
        
def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
