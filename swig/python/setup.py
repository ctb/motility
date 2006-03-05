from distutils.core import setup, Extension

# the c++ extension module (needs to be linked in with libmotility...)
extension_mod = Extension("_motility_extmodule",
                          ["_motility_extmodule.cc",],
                          include_dirs=['../../src',],
                          library_dirs=['../../src', '../'],
                          libraries=['interface', 'motility', 'stdc++'])

setup(name = "motility_ext", version="blah", ext_modules=[extension_mod])
