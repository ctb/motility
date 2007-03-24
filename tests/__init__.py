import sys
import os.path

#
# get the current directory from __file__
#

testdir = os.path.abspath(os.path.dirname(__file__))

#
# now build motility's python build/lib directory path
#

motility_build_dir = os.path.abspath(testdir + '/../python/')

#
# put it in the path
#

sys.path.insert(0, motility_build_dir)

import motility
#assert paircomp.__version__ == "1.1"

def motility_version_message():
    print """
Testing version %s of the motility Python extension module, loaded from

\t%s
""" % (paircomp.__version__, paircomp_build_dir,)
