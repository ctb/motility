#! /usr/bin/env python
import motility

###

def test_1():
    assert len(motility.find_iupac("ACTGNX", "N")) == 6

def test_2():
    failure = 1
    try:
        motility.find_iupac("R", "N");
        failure = 0
    except Exception, e:
        pass
    assert failure

def test_3():
    matrix = \
           [ [ 0.000, 0.026, 0.675, 1.050 ],
             [ 0.000, 1.653, 1.730, 1.561 ],
             [ 1.527, 2.859, 0.000, 1.850 ],
             [ 3.386, 3.755, 0.000, 3.569 ],
             [ 3.517, 3.667, 3.875, 0.000 ],
             [ 0.000, 1.876, 0.628, 1.988 ],
             [ 0.000, 1.705, 2.189, 1.333 ],
             [ 1.153, 2.193, 0.000, 1.670 ],
             [ 0.447, 1.020, 1.222, 0.000 ], ]

    operator = motility.EnergyOperator(matrix)
    
def test_4():
    """
    Test misc coord handling / match str extraction
    """
    motif = 'ACGG'
    
    pwm = motility.make_pwm([motif])
    pwm_match = pwm.find(motif, 4)
    iupac_match = motility.find_iupac(motif, motif)
    exact_match = motility.find_exact(motif, motif)

    assert pwm_match == iupac_match
    assert pwm_match == exact_match

    rcmotif = 'CCGT'

    pwm_match = pwm.find(rcmotif, 4)
    iupac_match = motility.find_iupac(rcmotif, motif)
    exact_match = motility.find_exact(rcmotif, motif)

    assert pwm_match == iupac_match

def test_5():
    """
    Test calc_score & calc_energy equivalence
    """
    motif = 'ACGG'
    
    pwm = motility.make_pwm([motif])
    operator = motility.make_operator([motif])

    print pwm.calc_score(motif)

    print operator.calc_score(motif)
    print operator.calc_energy(motif)
    assert operator.calc_score(motif) == operator.calc_energy(motif)
