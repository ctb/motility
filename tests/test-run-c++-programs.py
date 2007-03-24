#! /usr/bin/env python
import tests
from subprocess import *

def run_program(cmd):
    print '*** running: %s' % (cmd,)
    returncode = call(cmd, stdout=PIPE, stderr=PIPE)
    assert returncode == 0, '%s failed: %d' % (cmd, returncode)
    

def test():
    for program in ('test-find-iupac',
                    'test-find-literal',
                    'test-find-op',
                    'test-find-pwm',
                    'test-sequence'):
        cmd = '%s/%s' % (tests.testdir, program,)
        yield run_program, cmd
