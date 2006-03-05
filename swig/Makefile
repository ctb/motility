CXXFLAGS=-I../src/

all: libinterface.a perl_module python_module

clean:
	find . \( -name \*.o -o -name \*.so \) -exec rm {} \;
	rm -fr python/build
	rm -fr perl/blib
	rm -f perl/_motility_extmodule.cc python/_motility_extmodule.cc
	rm -f perl/motility_ext.{bs,pm} python/motility_ext.py
	rm -f libinterface.a

### basic interface

libinterface.a: interface.o
	ar rcv libinterface.a interface.o
	ranlib libinterface.a

interface.o: interface.cc interface.hh

### Perl stuff.

perl_module: perl/_motility_extmodule.o
	cd perl/ && make -f Makefile.bootstrap all && make
	cd ../

perl/_motility_extmodule.o: perl/_motility_extmodule.cc
	cd perl && perl Makefile.PL && make
	cd ../

perl/_motility_extmodule.cc: motility.i motility_pl.i interface.hh
	swig -perl -c++ -o perl/_motility_extmodule.cc motility.i

perl/motility_extmodule.py: motility.i motility_pl.i interface.hh
	swig -perl -c++ -o perl/_motility_extmodule.cc motility.i

### Python stuff.

python_module: python/_motility_extmodule.cc
	cd python && python setup.py build
	cd ../

python/_motility_extmodule.cc: motility.i motility_py.i interface.hh
	swig -python -c++ -o python/_motility_extmodule.cc motility.i

python/motility_ext.py: motility.i motility_py.i interface.hh

