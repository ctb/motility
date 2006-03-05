"""
Inform the test scripts of the path to motility's Python ext module.

This is cross platform.
"""

import sys
import os.path
import distutils.util
import platform

#
# get the current directory from __file__
#

testdir = os.path.abspath(os.path.dirname(__file__))

#
# now build motility's python build/lib directory path
#

platform_str = distutils.util.get_platform()
version = ".".join(platform.python_version_tuple()[:2])
motility_build_dir = testdir + '/../python/build/lib.%s-%s' % (platform_str,
                                                               version)
motility_build_dir = os.path.abspath(motility_build_dir)

#
# put it in the path
#

sys.path.insert(0, motility_build_dir)

import motility
assert motility.__version__ == "0.7"

def motility_version_message():
    print """
Testing version %s of the motility extension module, loaded from

\t%s
""" % (motility.__version__, motility_build_dir,)


