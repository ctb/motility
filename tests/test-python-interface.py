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
