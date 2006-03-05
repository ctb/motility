CXXFLAGS=-g -O2

all: libmotility.a

clean:
	rm -f *.o *.a

OBJS=DnaSequence.o motility.o LiteralMotif.o _MatrixMotif.o \
	PwmMotif.o IupacMotif.o EnergyOperator.o

libmotility.a: $(OBJS)
	ar rcv libmotility.a $(OBJS)
	ranlib libmotility.a

depend:
	makedepend -fMakefile.deps -- -I/usr/local/include $(CXXFLAGS) -- *.cc

include Makefile.deps
