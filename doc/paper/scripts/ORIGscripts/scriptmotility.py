#!/usr/bin/env python

# Do your motility stuff.




import datetime
import motility, Bio, TAMO

from Bio import Motif

print "This works!"


starttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
endtime = datetime.datetime.now( )

print endtime - starttime


print "Motility exact matches!"

starttime = datetime.datetime.now( )

print motility.find_exact(sequence, "TATAA")

print motility.find_exact(sequence, "GTTCGGCG")
print motility.find_exact(sequence, "CAAATGCA")
print motility.find_exact(sequence, "TGCCGCGC")
print motility.find_exact(sequence, "TGGCGAAG")
print motility.find_exact(sequence, "CCAACGTG")
print motility.find_exact(sequence, "AATCGGGT")
print motility.find_exact(sequence, "GTAATCAA")
print motility.find_exact(sequence, "TATTTTTT")
print motility.find_exact(sequence, "ATTATCCG")
print motility.find_exact(sequence, "TTGTCTAA")

	
print motility.find_exact(sequence, "TTTTTAAAAAAA")
print motility.find_exact(sequence, "TTGCGGCCCGTG")
print motility.find_exact(sequence, "ATCAGTGGGAAC")
print motility.find_exact(sequence, "GGCGATATCAAC")
print motility.find_exact(sequence, "ATACATGAGGTT")
print motility.find_exact(sequence, "TTGTATAAAAAT")
print motility.find_exact(sequence, "GTGACCAAAGAG")
print motility.find_exact(sequence, "ATCCGCATTCCG")
print motility.find_exact(sequence, "GTAATAGGACTG")
print motility.find_exact(sequence, "TACCCTGTGAGA")
print motility.find_exact(sequence, "CGTTTTCTGCGT")

print motility.find_exact(sequence, "TTACCACGATATTGGGCAGC")
print motility.find_exact(sequence, "CTTTATTGAAGCGGGTGATC")
print motility.find_exact(sequence, "GGTCTGCACTTTGCGCGCGT")
print motility.find_exact(sequence, "TATGTTGGCAATATTGATGA")
print motility.find_exact(sequence, "AACGATACCGTGCCACGTTT")
print motility.find_exact(sequence, "CAGCTCCGGCAGCGTATAGC")
print motility.find_exact(sequence, "CATCGATTCTTTAGCAGTGA")
print motility.find_exact(sequence, "TGCCTCGGGAGGCATTATTC")
print motility.find_exact(sequence, "TTATCATTGCCGCTATCCTG")
print motility.find_exact(sequence, "GGTTCTACGATTCTTAAGCC")

print motility.find_exact(sequence, "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA")


endtime = datetime.datetime.now( )
print endtime - starttime


print "end Motility exact matches!"

