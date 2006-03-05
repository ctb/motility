CXXFLAGS=-I../src/ -g

BIN=test-sequence test-find-literal test-find-pwm test-find-iupac \
	test-find-op

all: $(BIN)

clean:
	rm $(BIN)

test-sequence: test-sequence.cc ../src/libmotility.a

test-find-literal: test-find-literal.cc ../src/libmotility.a

test-find-pwm: test-find-pwm.cc ../src/libmotility.a

test-find-iupac: test-find-iupac.cc ../src/libmotility.a

test-find-op: test-find-op.cc ../src/libmotility.a
