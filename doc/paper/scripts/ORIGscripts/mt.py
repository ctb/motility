#!/usr/bin/env python

# Do your tamo stuff.


import datetime
import TAMO

from TAMO import MotifTools

print "This works!"


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )


print "tamo IUPAC matches!"
starttime = datetime.datetime.now( )
starttimeiupac = datetime.datetime.now( )

ms1 = MotifTools.Motif_from_text('WGATAR')
print ms1.oneletter
#print ms1.scan(sequence) 
print ms1.maxscore, ms1.maxscore *0.8

if (pamlist = ms1.bestscan(sequence)) > ms1.maxscore *0.8:print "Match! "

print pamlist

endtimeiupac = datetime.datetime.now( )

endtime = datetime.datetime.now( )

print "end TAMO IUPAC matches!"
print sequenceendtime - sequencestarttime

print endtimeiupac - starttimeiupac
print endtime - starttime
