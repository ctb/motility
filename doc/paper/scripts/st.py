#!/usr/bin/env python

# tamo st.py.

import datetime
import TAMO

from TAMO import MotifTools

sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )

outputfile = open ("OUTPUT/st.out", "w", 1)

starttimetata = datetime.datetime.now( )

ms1 = MotifTools.Motif_from_text('TATAA')
print >> outputfile,  ms1.oneletter
print >> outputfile,  ms1.scan(sequence) 
ms1r = MotifTools.Motif_from_text('AATAT')
print >> outputfile,  ms1r.oneletter
print >> outputfile,  ms1r.scan(sequence) 
#ms1c = MotifTools.Motif_from_text('ATATT')
#print ms1c.oneletter
#print ms1c.scan(sequence) 
#ms1rc = MotifTools.Motif_from_text('TTATA')
#print ms1rc.oneletter
#print ms1rc.scan(sequence) 

endtimetata = datetime.datetime.now( )
starttimesmall = datetime.datetime.now( )

ms2= MotifTools.Motif_from_text('GTTCGGCG')
print >> outputfile,  ms2.oneletter
print >> outputfile,  ms2.scan(sequence) 
#ms2c= MotifTools.Motif_from_text('CAAGCCGC')
#print ms2c.oneletter
#print ms2c.scan(sequence) 
ms2r= MotifTools.Motif_from_text('GCGGCTTG')
print >> outputfile,  ms2r.oneletter
print >> outputfile,  ms2r.scan(sequence) 
#ms2rc= MotifTools.Motif_from_text('CGCCGAAC')
#print ms2rc.oneletter
#print ms2rc.scan(sequence) 

endtimesmall = datetime.datetime.now( )
starttimemedium = datetime.datetime.now( )
ms12= MotifTools.Motif_from_text('TTTTTAAAAAAA')
print >> outputfile,  ms12.oneletter
print >> outputfile,  ms12.scan(sequence) 
#ms12c= MotifTools.Motif_from_text('AAAAATTTTTTT')
#print ms12c.oneletter
#print ms12c.scan(sequence) 
#ms12r= MotifTools.Motif_from_text('TTTTTTTAAAAA')
#print ms12r.oneletter
#print ms12r.scan(sequence) 
ms12rc= MotifTools.Motif_from_text('AAAAAAATTTTT')
print >> outputfile,  ms12rc.oneletter
print >> outputfile,  ms12rc.scan(sequence) 

endtimemedium = datetime.datetime.now( )
starttimelarge = datetime.datetime.now( )
ms23= MotifTools.Motif_from_text('TTACCACGATATTGGGCAGC')
print >> outputfile,  ms23.oneletter
print >> outputfile,  ms23.scan(sequence) 
#ms23c= MotifTools.Motif_from_text('AATGGTGCTATAACCCGTCG')
#print ms23c.oneletter
#print ms23c.scan(sequence) 
ms23r= MotifTools.Motif_from_text('CGACGGGTTATAGCACCATT')
print >> outputfile,  ms23r.oneletter
print >> outputfile,  ms23r.scan(sequence) 
#ms23rc= MotifTools.Motif_from_text('GCTGCCCAATATCGTGGTAA')
#print ms23rc.oneletter
#print ms23rc.scan(sequence) 
endtimelarge = datetime.datetime.now( )
starttimeverylarge = datetime.datetime.now( )

ms24= MotifTools.Motif_from_text('TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA')
print >> outputfile,  ms24.oneletter
print >> outputfile,  ms24.scan(sequence) 
#ms24c= MotifTools.Motif_from_text('CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT')
#print ms24c.oneletter
#print ms24c.scan(sequence) 
ms24r= MotifTools.Motif_from_text('ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT')
print >> outputfile,  ms24r.oneletter
print >> outputfile,  ms24r.scan(sequence) 
#ms24rc= MotifTools.Motif_from_text('TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA')
#print ms24rc.oneletter
#print ms24rc.scan(sequence) 
endtimeverylarge = datetime.datetime.now( )


timing = open ("OUTPUT/st.time", "w", 1)

print >> timing,  "end TAMO exact matches!"
print >> timing,  "TATA times: ", endtimetata - starttimetata
print >> timing,  "Small times: ", endtimesmall - starttimesmall
print >> timing,  "Medium times: ", endtimemedium - starttimemedium
print >> timing,  "Large times: ", endtimelarge - starttimelarge
print >> timing,  "very Large times: ", endtimeverylarge - starttimeverylarge
