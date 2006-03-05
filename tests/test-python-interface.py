#! /usr/bin/env python
import _testdir
_testdir.motility_version_message()

import motility

###

assert len(motility.find_iupac("ACTGNX", "N")) == 6

failure = 1
try:
    motility.find_iupac("R", "N");
    failure = 0
except Exception, e:
    pass

assert failure
