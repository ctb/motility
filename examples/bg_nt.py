"""
A simple example of a way to correct for background nt frequencies in
PWM calculations by biasing against more common sites.
"""

import motility
import math

class BackgroundAdjustedPWM(motility.PWM):
    def weight_sites_over(self, *args, **kwargs):
        raise Exception("you cannot use this method in bg-adjusted PWMs")

default_frequencies = dict(A=.25, C=.25, G=.25, T=.25)
def make_bg_pwm(sites, frequencies=default_frequencies):
    """
    Build a PWM according to Stormo, 2000, eqn 4; modify f_{b,i} with
    pseudocounts by adding +1.
    """
    # validate 'frequencies' dict
    if len(frequencies.keys()) != 4 or sum(frequencies.values()) != 1.0 \
       or not ('A' in frequencies and 'G' in frequencies and \
               'C' in frequencies and 'T' in frequencies):
        raise Exception("passed in frequencies dict must have values for A,C,G,T only, and the values must sum to 1")

    a_freq = float(frequencies['A'])
    c_freq = float(frequencies['C'])
    g_freq = float(frequencies['G'])
    t_freq = float(frequencies['T'])

    ###

    base_counts = motility.build.count_bases_by_position(sites)

    matrix = []
    for d in base_counts:
        column = [d[ch] for ch in 'ACGT']
        a, c, g, t = column
        n_sites = sum(column)

        a = math.log(float(a + 1) / float(n_sites + 1) / a_freq, 2)
        c = math.log(float(c + 1) / float(n_sites + 1) / c_freq, 2)
        g = math.log(float(g + 1) / float(n_sites + 1) / g_freq, 2)
        t = math.log(float(t + 1) / float(n_sites + 1) / t_freq, 2)

        column = [ a, c, g, t ]
        
        # normalize
        norm_factor = min(column)
        column = [ x - norm_factor for x in column ]
        matrix.append(column)

    return BackgroundAdjustedPWM(matrix)

###

sites = [ 'AGATAA',
          'AGATAG' ]

# if AT is more common than GC, the PWM should score a GC-rich site
# higher because it is less likely to occurr at random.

pwm = make_bg_pwm(sites)
bg_pwm = make_bg_pwm(sites, dict(A=.35, C=.15, G=.15, T=.35))

site = 'AGATAA'
site2 = 'AGATAG'

# the scores under the AT==GC model should be equivalent
assert pwm.calc_score(site) == pwm.calc_score(site2)

# the score for 'site' (higher AT) should be less than the score for
# 'site2' (higher GC).
assert bg_pwm.calc_score(site) < bg_pwm.calc_score(site2)
