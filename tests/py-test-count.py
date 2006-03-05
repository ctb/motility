#! /usr/bin/env python2.3
import _testdir

import motility

###
### note, by default 'N's are ignored by the following code.
###

matrix = [ [ .5, 1.0, 1.0, 1.0, 100. ],
           [ 1.0, 0, 1.0, 1.0, 100. ],
           [ 1.0, 1.0, 0, 1.0, 100. ],
           [ 1.0, 1.0, 4.0, 0, 100. ],
           [ 0, 1.0, 1.0, 1.0, 100. ],
           [ .5, 1.0, 1.0, 1.0, 100. ] ]

operator = motility.EnergyOperator(matrix)
calc_under_6 = operator.generate_sites_under(6)

pwm = motility.PWM(matrix)

calc_over_8 = pwm.generate_sites_over(8)

def calc_min(mat):
    return sum(map(min, mat))

def calc_max(mat):
    mat = [ i[:4] for i in mat ]        # eliminate 'N's
    return sum(map(max, mat))

assert calc_min(matrix) == operator.min_score()
assert calc_max(matrix) == operator.max_score()

assert calc_min(matrix) == pwm.min_score()
assert calc_max(matrix) == pwm.max_score()

####

alphabet = ('A', 'C', 'G', 'T')

def rN(L, d={}, *args):
    """
    Generate all L-tuples from the given alphabet.
    """
    if L == 0:
        d["".join(args)] = 1
        return

    for letter in alphabet:
        rN(L-1, d, letter, *args)

    return d.keys()

all_sites = rN(len(matrix))

above_8 = [ site for site in all_sites if pwm.calc_score(site) >= 8 ]
under_6 = [ site for site in all_sites if operator.calc_energy(site) <= 6 ]

calc_over_8 = list(calc_over_8)
calc_under_6 = list(calc_under_6)

above_8.sort()
calc_over_8.sort()

assert above_8 == calc_over_8

min_score = int(pwm.min_score() - 2)
max_score = int(pwm.max_score() + 2)

def calc_sitelist_weight(sites, AT_bias, GC_bias):
    pd = dict(A=AT_bias, C=GC_bias, G=GC_bias, T=AT_bias)

    total = 0.
    for site in sites:
        weight = 1.0
        for ch in site:
            weight *= pd[ch]

        total += weight

    return total

for threshold in range(min_score, max_score):
    predicted_under = operator.generate_sites_under(threshold)
    predicted_over = pwm.generate_sites_over(threshold)

    for (AT_bias, GC_bias) in ((.75 / 2., .25 / 2.),
                               (.5 / 2., .5 / 2.),
                               (.25 / 2., .75 / 2.)):

        pred_u_weight = operator.weight_sites_under(threshold, AT_bias,
                                                    GC_bias)
        calc_u_weight = calc_sitelist_weight(predicted_under, AT_bias, GC_bias)

        assert pred_u_weight == calc_u_weight
        
        pred_o_weight = pwm.weight_sites_over(threshold, AT_bias, GC_bias)
        calc_o_weight = calc_sitelist_weight(predicted_over, AT_bias, GC_bias)

        assert pred_o_weight == calc_o_weight

    calc_under = [ i for i in all_sites \
                   if operator.calc_energy(i) <= threshold ]
    calc_over = [ i for i in all_sites \
                  if pwm.calc_score(i) >= threshold ]

    predicted_under = list(predicted_under)
    predicted_over = list(predicted_over)

    predicted_under.sort()
    predicted_over.sort()

    calc_under.sort()
    calc_over.sort()

    assert predicted_under == calc_under
    assert predicted_over == calc_over

print 'ALL TESTS PASSED.'
