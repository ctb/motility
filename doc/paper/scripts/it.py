#!/usr/bin/env python

# tamo it.py, IUPAC SEARCHES


import datetime
import TAMO

from TAMO import MotifTools

#sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
#sequenceendtime = datetime.datetime.now( )


outfile = open("OUTPUT/it.out", "w")

starttimeiupac = datetime.datetime.now( )

ms1 = MotifTools.Motif_from_text('WGATAR')
print >> outfile,  ms1.oneletter
print >> outfile, ms1.scan(sequence) 

endtimeiupac = datetime.datetime.now( )


timefile = open("OUTPUT/it.time", "w")

print >> timefile, "TAMO IUPAC matches!"
Deltatime = endtimeiupac - starttimeiupac
print  >>timefile,  "tamo IUPAC TIME: ",  endtimeiupac - starttimeiupac

