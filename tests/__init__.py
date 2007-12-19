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
print motility
assert motility.__version__ == "0.8.2", motility.__version__

def motility_version_message():
    print """
Testing version %s of the motility Python extension module, loaded from

\t%s
""" % (motility.__version__, motility_build_dir,)
