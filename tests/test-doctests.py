"""
Run various doctests; at least for the moment, files containing doctests
have to be manually added, bleah.

Note that this file can be run from the command line and from within nose,
both. When run from within nose, however, doctests from each module or
file show up as only a single test.
"""

import doctest
import os.path

thisdir = os.path.dirname(__file__)

def test_tutorial(raise_on_error=True):
    tutorial = os.path.join(thisdir, '../doc/python-tutorial.txt')
    tutorial = os.path.abspath(tutorial)

    doctest.testfile(tutorial, module_relative=False,
                     raise_on_error=raise_on_error)

def test_motility_py(raise_on_error=True):
    import motility.build
    doctest.testmod(motility.build, raise_on_error=raise_on_error)

if __name__ == '__main__':
    import sys
    motility_build_dir = os.path.abspath(thisdir + '/../python/')
    sys.path.insert(0, motility_build_dir)

    import motility

    # make sure we got the right module: the development one.
    module_abs = os.path.abspath(os.path.dirname(motility.__file__))
    dotdot_abs = os.path.abspath(os.path.join(thisdir, '../'))
    assert dotdot_abs in module_abs, "not testing the development motility..."

    print 'testing tutorial; silence means goodness'
    test_tutorial(raise_on_error=False)

    print 'testing motility python doctests; silence means goodness'
    test_motility_py(raise_on_error=False)
