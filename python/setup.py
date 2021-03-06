#! /usr/bin/env python
try:
   from setuptools import setup, Extension
except ImportError:
   from distutils.core import setup, Extension

# the c++ extension module (needs to be linked in with libmotility...)
extension_mod = Extension("motility._motilitymodule",
                          ["_motilitymodule.cc"],
                          include_dirs=['../src',],
                          library_dirs=['../src',],
                          libraries=['motility', 'stdc++'],
                          depends=['../src/libmotility.a',],
                          extra_link_args=['-fPIC'],
                          )

# python modules: currently only 'motility.py'
py_mod = 'motility'

setup(name = "motility", version = "0.8.2",
      description = 'Motility motif searching library',
      author = 'C. Titus Brown',
      author_email = 'titus@caltech.edu',
      url = 'http://cartwheel.caltech.edu/',
      packages = ['motility',],
      ext_modules = [extension_mod,],
      test_suite = 'nose.collector'
      )
