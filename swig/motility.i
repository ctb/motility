%module motility_ext

%{
#include <iostream>
#include "../interface.hh"
%}

## adding a new language.
##
## the following typemaps are needed for each new language:
##
## %typemap(out) motility::MotifMatchList*
## %typemap(in) _DoubleMatrix*
##
## see 'motility_py.i' for examples...

%include "motility_py.i"	# python typemaps
%include "motility_pl.i"	# perl typemaps

##
## these two typemaps are responsible for freeing the C++ structures
## returned by the interface functions & should be the same for all
## languages.
##

%typemap(freearg) motility::MotifMatchList* {
    if ($1) { delete $1; }
}

%typemap(freearg) _DoubleMatrix * {
    if ($1) { free($1->_matrix); free($1); }
}

## finally -- include the actual interface!

%include "interface.hh"
