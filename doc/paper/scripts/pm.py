#!/usr/bin/env python

# Motility Position Weight searches.

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

outputfile = open("OUTPUT/pm.out", "w", 1)


starttimepm = datetime.datetime.now( )

sites = [ 'AGATAA',
	  'TGATAA',
	  'AGATAG' ]

print >> outputfile,  motility.make_iupac_motif(sites)

pwm = motility.make_pwm(sites)
print >> outputfile,  pwm.max_score(), pwm.min_score()

#print >> outputfile,  pwm.find(sequence, 10.57)
countlist =  pwm.find(sequence, 10.57)
print len(countlist)

for site in ['AGATAA', 'TGATAA', 'AGATAG']:
	print >> outputfile,  site, pwm.calc_score(site)

matrix_tuple = ((1, 0, 0, 1),
		(0, 0, 1, 0),
		(1, 0, 0, 0),
		(0, 0, 0, 1),
		(1, 0, 0, 0),
		(1, 0, 1, 0))


matrix = motility.PWM(matrix_tuple)

matrix.generate_sites_over(6.0)

#print >> outputfile,  matrix.find(sequence, 10.57)
countlist2 =  pwm.find(sequence, 10.57)
print len(countlist2)

endtimepm = datetime.datetime.now( )


timefile = open("OUTPUT/pm.time", "w", 1)

print >> timefile,  "end Motility Position Weight matches"
print >> timefile,  "Motility PM: ", endtimepm - starttimepm

