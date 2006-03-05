# put specific version # in if you want.
PYTHON=python

### shouldn't need to change anything below here ###

all: src-dir tests-dir python-dir

install: all
	cd python-dir/ && $(PYTHON) setup.py install
	cd ../

clean:
	find . -name \*.o -exec rm {} \;
	find . -name \*.a -exec rm {} \;
	find . -name \*.so -exec rm {} \;
	cd tests && $(MAKE) clean
	cd ../

src-dir:
	cd src && $(MAKE)
	cd ../

tests-dir:
	cd tests && $(MAKE)
	cd ../

python-dir:
	cd python && $(PYTHON) setup.py build
