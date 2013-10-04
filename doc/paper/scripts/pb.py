#!/usr/bin/env python

# Biopython position weight matrix.


import datetime
import Bio

from Bio import Motif
from Bio.Alphabet import IUPAC

#sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
#sequenceendtime = datetime.datetime.now( )

#
# This is from BioPython
#
#

from Bio.Seq import Seq

from Bio.Alphabet import IUPAC

outputfile = open("OUTPUT/pb.out", "w", 1)
starttimepm = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("AGATAA",s1.alphabet))
s1.add_instance(Seq("AGATAG",s1.alphabet))
s1.add_instance(Seq("TGATAA",s1.alphabet))
s1.add_instance(Seq("TGATAG",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)


for pos, score, in s1.search_pwm(test_seq, threshold=9.72):
	print >> outputfile, pos, score

def rev(s) : return s[::-1]

rev_test_seq = rev(test_seq)

for pos, score, in s1.search_pwm(rev_test_seq, threshold=9.72):
	print >> outputfile, pos, score

endtimepm = datetime.datetime.now( )

timefile = open ("OUTPUT/pb.time", "w", 1)

print >> timefile, "Biopyhton Position Weight matrix matches!"
print >> timefile, "Biopython PWM match time: ", endtimepm - starttimepm
