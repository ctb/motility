#!/usr/bin/env python

# Position Weight Tamo.


import datetime
import TAMO
import motility

from TAMO import MotifTools

#sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
#sequenceendtime = datetime.datetime.now( )

starttimepm = datetime.datetime.now( )

outputfile = open("OUTPUT/pt.out", "w", 1)

ms1 = MotifTools.Motif_from_text('WGATAR')
print >>outputfile, ms1.oneletter
#print ms1.scan(sequence) 
print >>outputfile, ms1.maxscore, ms1.maxscore *0.8

print >>outputfile, ms1.bestscan(sequence) 
pwlist =  ms1.bestseqs(9.72) 

#
if pwlist :
	pwmember = pwlist.pop()

sites = ['XXXXXXXXXX', 'XXXXXXXXXX', 'XXXXXXXXXX', 'XXXXXXXXXX' ]

i = 0
while pwmember :
	foundseq = pwmember[1]
	sites[i] = foundseq 
	i = i + 1
	print >> outputfile, foundseq  
	if pwlist:
		pwmember = pwlist.pop()
	else:
		pwmember = []


Iupaqseq = motility.make_iupac_motif(sites)
print >>outputfile, Iupaqseq 

tqs = MotifTools.Motif_from_text(Iupaqseq)
print >>outputfile, tqs.oneletter
print >>outputfile, tqs.scan(sequence) 

def rev(s) : return s[::-1]

Iupaqseq = rev(Iupaqseq)
print >>outputfile, Iupaqseq

tqs2 = MotifTools.Motif_from_text(Iupaqseq)
print >>outputfile, tqs2.oneletter
print >>outputfile, tqs2.scan(sequence) 

endtimepm = datetime.datetime.now( )


timefile = open("OUTPUT/mt.time", "w", 1)

print >> timefile, "TAMO position weight seach"
print >> timefile, "TAMO PM time: ", endtimepm - starttimepm
