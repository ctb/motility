"""
A simple example of one way to correct for background nt frequencies in
PWM calculations.
"""

import motility
import math

class BackgroundAdjustedPWM(motility.PWM):
    def weight_sites_over(self, *args, **kwargs):
        raise Exception("you cannot use this method in bg-adjusted PWMs")

default_frequencies = dict(A=.25, C=.25, G=.25, T=.25)
def make_bg_pwm(sites, frequencies=default_frequencies):
    # validate 'frequencies' dict
    if len(frequencies.keys()) != 4 or sum(frequencies.values()) != 1.0 \
       or not ('A' in frequencies and 'G' in frequencies and \
               'C' in frequencies and 'T' in frequencies):
        raise Exception("passed in frequencies dict must have values for A,C,G,T only, and the values must sum to 1")
    
    # x = base count, y = max count
    cell_fn = lambda x, y, z: math.log((float(x) + 1) / (float(y) + 1), 2)
    matrix = motility.make_matrix(sites, cell_fn, None, normalize=True)

    # now, adjust matrix for observed frequencies of nts in genome:
    adjusted = []
    for (a, c, g, t) in matrix:
        a *= 0.25 / float(frequencies['A'])
        c *= 0.25 / float(frequencies['C'])
        g *= 0.25 / float(frequencies['G'])
        t *= 0.25 / float(frequencies['T'])

        adjusted.append((a, c, g, t))

    return BackgroundAdjustedPWM(adjusted)

###

sites = [ 'AGATAA',
          'TGATAA',
          'AGATAG' ]

pwm = motility.make_pwm(sites)

##

bg_pwm = make_bg_pwm(sites)

# equal, if no frequency dict given.
assert pwm.calc_score(sites[0]) == bg_pwm.calc_score(sites[0])

##

bg_pwm = make_bg_pwm(sites, dict(A=.35, C=.15, G=.15, T=.35))

# should score AT-rich sites lower, and GC-rich sites higher
site = 'AAAAAA'
assert bg_pwm.calc_score(site) < pwm.calc_score(site)

site = 'GGGGGG'
assert bg_pwm.calc_score(site) > pwm.calc_score(site)

