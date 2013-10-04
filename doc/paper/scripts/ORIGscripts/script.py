#!/usr/bin/env python

import datetime

starttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
endtime = datetime.datetime.now( )

print endtime - starttime

print "python exact matches!"


starttime = datetime.datetime.now( )


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TATAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TATAA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AATAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AATAT " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("GTTCGGCG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1 

print "GTTCGGCG " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("GCGGCTTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1 

print "GCGGCTTG " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CAAATGCA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CAAATGCA " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TGCCGCGC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TGCCGCGC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CGCGCCGT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CGCGCCGT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TGGCGAAG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TGGCGAAG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GAAGCGGT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GAAGCGGT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CCAACGTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CCAACGTG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GTGCAACC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GTGCAACC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("AATCGGGT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AATCGGGT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TGGGCTAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TGGGCTAA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GTAATCAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GTAATCAA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("AACTAATG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AACTAATG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TATTTTTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TATTTTTT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTTTTTAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTTTTTAT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("ATTATCCG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATTATCCG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GCCTATTA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GCCTATTA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTGTCTAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTGTCTAA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("AATCTGTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AATCTGTT " , foundlocations



foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TTTTTAAAAAAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTTTTAAAAAAA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AAAAAAATTTTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AAAAAAATTTTT " , foundlocations


foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GTGCCCGGCGTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GTGCCCGGCGTT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTGCGGCCCGTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTGCGGCCCGTG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("ATCAGTGGGAAC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATCAGTGGGAAC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CAAGGGTGACTA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CAAGGGTGACTA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GGCGATATCAAC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GGCGATATCAAC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CAACTATAGCGG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CAACTATAGCGG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("ATACATGAGGTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATACATGAGGTT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTGGAGTACATA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTGGAGTACATA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTGTAGAAAAAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTGTAGAAAAAT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TAAAAAGATGTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TAAAAAGATGTT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GTGACCAAAGAG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GTGACCAAAGAG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GAGAAACCAGTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GAGAAACCAGTG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("ATCCGCATTCCG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATCCGCATTCCG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GCCTTACGCCTA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GCCTTACGCCTA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GTAATAGGACTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1
print "GTAATAGGACTG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GTCAGGATAATG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1
print "GTCAGGATAATG " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TACCCTGTGAGA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TACCCTGTGAGA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("AGAGTGTCCCAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AGAGTGTCCCAT " , foundlocations


foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CGTTTTCTGCGT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CGTTTTCTGCGT " , foundlocations


foundlocations = []
index = 0

# here
while (True) : 
	print index
	index = sequence.find("TGCGTCTTTTGC", index)
	print index
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "rev) TGCGTCTTTTGC " , foundlocations




foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTACCACGATATTGGGCAGC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTACCACGATATTGGGCAGC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CGACGGGTTATAGCACCATT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CGACGGGTTATAGCACCATT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CTTTATTGAAGCGGGTGATC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CTTTATTGAAGCGGGTGATC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CTAGTGGGCGAAGTTATTTC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CTAGTGGGCGAAGTTATTTC " , foundlocations


foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GGTCTGCACTTTGCGCGCGT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GGTCTGCACTTTGCGCGCGT " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TGCGCGCGTTTCACGTCTGG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TGCGCGCGTTTCACGTCTGG " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TATGTTGGCAATATTGATGA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TATGTTGGCAATATTGATGA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AGTAGTTATAACGGTTGTAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AGTAGTTATAACGGTTGTAT " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AACGATACCGTGCCACGTTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AACGATACCGTGCCACGTTT " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TTTGCACCGTGCCATAGCAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTTGCACCGTGCCATAGCAA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CAGCTCCGGCAGCGTATAGC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CAGCTCCGGCAGCGTATAGC " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CGATATGCGACGGCCTCGAC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CGATATGCGACGGCCTCGAC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CATCGATTCTTTAGCAGTGA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CATCGATTCTTTAGCAGTGA " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("AGTCACGATTTCTTAGCTAC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AGTCACGATTTCTTAGCTAC " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TGCCTCGGGAGGCATTATTC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TGCCTCGGGAGGCATTATTC " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CTTATTACGGAGGGCTCCGT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CTTATTACGGAGGGCTCCGT " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TTATCATTGCCGCTATCCTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTATCATTGCCGCTATCCTG " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("GTCCTATCGCCGTTACTATT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GTCCTATCGCCGTTACTATT " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("GGTTCTACGATTCTTAAGCC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GGTTCTACGATTCTTAAGCC " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CCGAATTCTTAGCATCTTGG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CCGAATTCTTAGCATCTTGG " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT " , foundlocations


endtime = datetime.datetime.now( )
print endtime - starttime

print "python exact matches!"

