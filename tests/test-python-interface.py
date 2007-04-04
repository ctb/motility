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
