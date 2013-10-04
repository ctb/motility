#!/usr/bin/env python

# IUPAC motility searches.

import datetime
import motility, Bio, TAMO

from Bio import Motif

#sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
#sequenceendtime = datetime.datetime.now( )

outputfile = open("OUTPUT/im.out", "w")


starttimeiupac = datetime.datetime.now( )

print >> outputfile,   motility.find_iupac(sequence, "WGATAR")
#countlist =   motility.find_iupac(sequence, "WGATAR")
#print len(countlist)

endtimeiupac = datetime.datetime.now( )

timefile = open("OUTPUT/im.time", "w")

print >> timefile, "End Motility iupac matches!"
#Deltatime = sequenceendtime - sequencestarttime
#print >>timefile,  "Sequence Read in Time: ", Deltatime
Deltatime = endtimeiupac - starttimeiupac
print >>timefile,  "Motility Iupac search time: ", Deltatime

