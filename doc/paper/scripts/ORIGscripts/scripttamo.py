#!/usr/bin/env python

# Do your tamo stuff.


import datetime
import TAMO

from TAMO import MotifTools

print "This works!"


starttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
endtime = datetime.datetime.now( )

print endtime - starttime


print "tamo exact matches!"

starttime = datetime.datetime.now( )


m = MotifTools.Motif_from_text('TATAA')
#print type (m), type(m.oneletter)
print m.oneletter
#print m.revcomp().oneletter
#print m.bestscore(sequence, fwd=' ')
#print m.bestscan(sequence)
#print m.bestscanseq(sequence)
print m.maxscore
print m.scan(sequence) #, threshold=5.0, factor = 0.69)





m01 = MotifTools.Motif_from_text("GTTCGGCG")
print m01.scan(sequence) #, threshold=5.0, factor = 0.69)
m02 = MotifTools.Motif_from_text("CAAATGCA")
print m02.scan(sequence) #, threshold=5.0, factor = 0.69)
m03 = MotifTools.Motif_from_text("TGCCGCGC")
print m03.scan(sequence) #, threshold=5.0, factor = 0.69)
m04 = MotifTools.Motif_from_text("TGGCGAAG")
print m04.scan(sequence) #, threshold=5.0, factor = 0.69)
m05 = MotifTools.Motif_from_text("CCAACGTG")
print m05.scan(sequence) #, threshold=5.0, factor = 0.69)
m06 = MotifTools.Motif_from_text("AATCGGGT")
print m06.scan(sequence) #, threshold=5.0, factor = 0.69)
m07 = MotifTools.Motif_from_text("GTAATCAA")
print m07.scan(sequence) #, threshold=5.0, factor = 0.69)
m08 = MotifTools.Motif_from_text("TATTTTTT")
print m08.scan(sequence) #, threshold=5.0, factor = 0.69)
m09 = MotifTools.Motif_from_text("ATTATCCG")
print m09.scan(sequence) #, threshold=5.0, factor = 0.69)
m10 = MotifTools.Motif_from_text("TTGTCTAA")
print m10.scan(sequence) #, threshold=5.0, factor = 0.69)

	
m11 = MotifTools.Motif_from_text("TTTTTAAAAAAA")
print m11.scan(sequence) #, threshold=5.0, factor = 0.69)
m12 = MotifTools.Motif_from_text("TTGCGGCCCGTG")
print m12.scan(sequence) #, threshold=5.0, factor = 0.69)
m13 = MotifTools.Motif_from_text("ATCAGTGGGAAC")
print m13.scan(sequence) #, threshold=5.0, factor = 0.69)
m14 = MotifTools.Motif_from_text("GGCGATATCAAC")
print m14.scan(sequence) #, threshold=5.0, factor = 0.69)
m15 = MotifTools.Motif_from_text("ATACATGAGGTT")
print m15.scan(sequence) #, threshold=5.0, factor = 0.69)
m16 = MotifTools.Motif_from_text("TTGTATAAAAAT")
print m16.scan(sequence) #, threshold=5.0, factor = 0.69)
m17 = MotifTools.Motif_from_text("GTGACCAAAGAG")
print m17.scan(sequence) #, threshold=5.0, factor = 0.69)
m18 = MotifTools.Motif_from_text("ATCCGCATTCCG")
print m18.scan(sequence) #, threshold=5.0, factor = 0.69)
m19 = MotifTools.Motif_from_text("GTAATAGGACTG")
print m19.scan(sequence) #, threshold=5.0, factor = 0.69)
m20 = MotifTools.Motif_from_text("TACCCTGTGAGA")
print m20.scan(sequence) #, threshold=5.0, factor = 0.69)
#
m21 = MotifTools.Motif_from_text("CGTTTTCTGCGT")
print m21.scan(sequence) #, threshold=5.0, factor = 0.69)

	
m22 = MotifTools.Motif_from_text("TTACCACGATATTGGGCAGC")
print m22.scan(sequence) #, threshold=5.0, factor = 0.69)
m23 = MotifTools.Motif_from_text("CTTTATTGAAGCGGGTGATC")
print m23.scan(sequence) #, threshold=5.0, factor = 0.69)
m24 = MotifTools.Motif_from_text("GGTCTGCACTTTGCGCGCGT")
print m24.scan(sequence) #, threshold=5.0, factor = 0.69)
m25 = MotifTools.Motif_from_text("TATGTTGGCAATATTGATGA")
print m25.scan(sequence) #, threshold=5.0, factor = 0.69)
m26 = MotifTools.Motif_from_text("AACGATACCGTGCCACGTTT")
print m26.scan(sequence) #, threshold=5.0, factor = 0.69)
m27 = MotifTools.Motif_from_text("CAGCTCCGGCAGCGTATAGC")
print m27.scan(sequence) #, threshold=5.0, factor = 0.69)
m28 = MotifTools.Motif_from_text("CATCGATTCTTTAGCAGTGA")
print m28.scan(sequence) #, threshold=5.0, factor = 0.69)
m29 = MotifTools.Motif_from_text("TGCCTCGGGAGGCATTATTC")
print m29.scan(sequence) #, threshold=5.0, factor = 0.69)
m30 = MotifTools.Motif_from_text("TTATCATTGCCGCTATCCTG")
print m30.scan(sequence) #, threshold=5.0, factor = 0.69)
m31 = MotifTools.Motif_from_text("GGTTCTACGATTCTTAAGCC")
print m31.scan(sequence) #, threshold=5.0, factor = 0.69)
#
m32 = MotifTools.Motif_from_text("TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA")
print m32.scan(sequence) #, threshold=5.0, factor = 0.69)


endtime = datetime.datetime.now( )
print endtime - starttime


print "end TAMO exact matches!"
