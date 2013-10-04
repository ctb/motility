#!/usr/bin/env python
# ib.py    IUPAC BIOPYTHON python script

import datetime
import Bio

from Bio import Motif
from Bio.Alphabet import IUPAC


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )

#
# This is from BioPython
#

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


starttimeiupac = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("AGATAA",s1.alphabet))
s1.add_instance(Seq("AGATAG",s1.alphabet))
s1.add_instance(Seq("TGATAA",s1.alphabet))
s1.add_instance(Seq("TGATAG",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)
endtimeiupac = datetime.datetime.now( )

fpresults = open("OUTPUT/ib.out", "w", 1)

startsearchtime = datetime.datetime.now( )
OutString = "(" 
fpresults.write (OutString)

firsttime = 1

for pos,seq in s1.search_instances(test_seq):
	if firsttime:
		PreOutString = ""
		firsttime = 0
	else:
		PreOutString = ","
	OutString = PreOutString + "(" + `pos` + " " + seq.tostring()+ ")"
	fpresults.write (OutString)

OutString = ")\n" 
fpresults.write (OutString)
endsearchtime = datetime.datetime.now( )



s2 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s2.add_instance(Seq("AATAGA",s2.alphabet))
s2.add_instance(Seq("GATAGA",s2.alphabet))
s2.add_instance(Seq("AAGATG",s2.alphabet))
s2.add_instance(Seq("GATAGT",s2.alphabet))
test_seq=Seq(sequence, s2.alphabet)
endtimeiupac = datetime.datetime.now( )


startsearchtime = datetime.datetime.now( )
OutString = "(" 
fpresults.write (OutString)

firsttime = 1

for pos,seq in s2.search_instances(test_seq):
	if firsttime:
		PreOutString = ""
		firsttime = 0
	else:
		PreOutString = ","
	OutString = PreOutString + "(" + `pos` + " " + seq.tostring()+ ")"
	fpresults.write (OutString)

OutString = ")\n" 
fpresults.write (OutString)
fpresults.close()


endsearchtime = datetime.datetime.now( )

timefile = open("OUTPUT/ib.time", "w")

print >> timefile, "Biopyhton exact matches done"
Deltatime = sequenceendtime - sequencestarttime
print >>timefile,  "Sequence Read in Time: ", Deltatime

Deltatime = endtimeiupac - starttimeiupac
print >>timefile,  "Iupac set up time: ", Deltatime

Deltatime = endsearchtime - startsearchtime
print >>timefile,  "Biopython search time: ",  Deltatime

