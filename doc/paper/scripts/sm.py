#!/usr/bin/env python

# motility sm.py

import datetime
import motility, Bio, TAMO

from Bio import Motif


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )

outputfile = open("OUTPUT/sm.out", "w", 1)


starttime = datetime.datetime.now( )
starttimetata = datetime.datetime.now( )

#print >> outputfile,  motility.find_exact(sequence, "TATAA")
tatacount =  motility.find_exact(sequence, "TATAA")
print len(tatacount)

#print motility.find_exact(sequence, "ATATT")
#print motility.find_exact(sequence, "TTATA")
endtimetata = datetime.datetime.now( )
starttimesmall = datetime.datetime.now( )
#print >> outputfile,  motility.find_exact(sequence, "GTTCGGCG")
gccount =  motility.find_exact(sequence, "GTTCGGCG")
print len(gccount)

#print motility.find_exact(sequence, "CAAGCCGC")
#print motility.find_exact(sequence, "CGCCGAAC")
endtimesmall = datetime.datetime.now( )
starttimemedium = datetime.datetime.now( )
print >> outputfile,  motility.find_exact(sequence, "TTTTTAAAAAAA")
#print motility.find_exact(sequence, "AAAAATTTTTTT")
#print motility.find_exact(sequence, "AAAAAAATTTTT")
endtimemedium = datetime.datetime.now( )
starttimelarge = datetime.datetime.now( )
print >> outputfile,  motility.find_exact(sequence, "TTACCACGATATTGGGCAGC")
#print motility.find_exact(sequence, "AATGGTGCTATAACCCGTCG")
#print motility.find_exact(sequence, "GCTGCCCAATATCGTGGTAA")
endtimelarge = datetime.datetime.now( )
starttimeverylarge = datetime.datetime.now( )
print >> outputfile,  motility.find_exact(sequence, "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA")
#print motility.find_exact(sequence, "CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT")
#print motility.find_exact(sequence, "TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA")
endtimeverylarge = datetime.datetime.now( )

endtime = datetime.datetime.now( )

timings = open ("OUTPUT/sm.time", "w", 1)

print >> timings, "Motility exact matches"
print >> timings, "TATAA Timings: ", endtimetata - starttimetata
print >> timings, "Small Timings: ", endtimesmall - starttimesmall
print >> timings, "Medium Timings: ", endtimemedium - starttimemedium
print >> timings, "Large Timings: ", endtimelarge - starttimelarge
print >> timings, "very Large Timings: ", endtimeverylarge - starttimeverylarge
