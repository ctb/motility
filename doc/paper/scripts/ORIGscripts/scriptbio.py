#!/usr/bin/env python

# Do your Biopython stuff.


import datetime
import Bio

from Bio import Motif

print "This works!"


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )

#
# This is from BioPython
#
#

print "Biopyhton exact matches!"

from Bio.Seq import Seq

from Bio.Alphabet import IUPAC

starttime = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("TATAA",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)
for pos,seq in s1.search_instances(test_seq):
	print pos,seq.tostring()

s2 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s2.add_instance(Seq("GTTCGGCG",s2.alphabet))
#test_seq=Seq(sequence, s2.alphabet)
for pos,seq in s2.search_instances(test_seq):
	print pos,seq.tostring()

s3 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s3.add_instance(Seq("CAAATGCA",s3.alphabet))
#test_seq=Seq(sequence, s3.alphabet)
for pos,seq in s3.search_instances(test_seq):
	print pos,seq.tostring()

s4 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s4.add_instance(Seq("TGCCGCGC",s4.alphabet))
#test_seq=Seq(sequence, s4.alphabet)
for pos,seq in s4.search_instances(test_seq):
	print pos,seq.tostring()

s5 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s5.add_instance(Seq("TGGCGAAG",s5.alphabet))
#test_seq=Seq(sequence, s5.alphabet)
for pos,seq in s5.search_instances(test_seq):
	print pos,seq.tostring()

s6 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s6.add_instance(Seq("CCAACGTG",s6.alphabet))
#test_seq=Seq(sequence, s6.alphabet)
for pos,seq in s6.search_instances(test_seq):
	print pos,seq.tostring()

s7 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s7.add_instance(Seq("AATCGGGT",s7.alphabet))
#test_seq=Seq(sequence, s7.alphabet)
for pos,seq in s7.search_instances(test_seq):
	print pos,seq.tostring()

s8 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s8.add_instance(Seq("GTAATCAA",s8.alphabet))
#test_seq=Seq(sequence, s8.alphabet)
for pos,seq in s8.search_instances(test_seq):
	print pos,seq.tostring()

s9 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s9.add_instance(Seq("TATTTTTT",s9.alphabet))
#test_seq=Seq(sequence, s9.alphabet)
for pos,seq in s9.search_instances(test_seq):
	print pos,seq.tostring()

s10 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s10.add_instance(Seq("ATTATCCG",s10.alphabet))
#test_seq=Seq(sequence, s10.alphabet)
for pos,seq in s10.search_instances(test_seq):
	print pos,seq.tostring()

s11 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s11.add_instance(Seq("TTGTCTAA",s11.alphabet))
#test_seq=Seq(sequence, s11.alphabet)
for pos,seq in s11.search_instances(test_seq):
	print pos,seq.tostring()
#
# medium searches
#

s12 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s12.add_instance(Seq("TTTTTAAAAAAA",s12.alphabet))
#test_seq=Seq(sequence, s12.alphabet)
for pos,seq in s12.search_instances(test_seq):
	print pos,seq.tostring()

s13 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s13.add_instance(Seq("TTGCGGCCCGTG",s13.alphabet))
#test_seq=Seq(sequence, s13.alphabet)
for pos,seq in s13.search_instances(test_seq):
	print pos,seq.tostring()

s14 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s14.add_instance(Seq("ATCAGTGGGAAC",s14.alphabet))
#test_seq=Seq(sequence, s14.alphabet)
for pos,seq in s14.search_instances(test_seq):
	print pos,seq.tostring()

s15 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s15.add_instance(Seq("GGCGATATCAAC",s15.alphabet))
#test_seq=Seq(sequence, s15.alphabet)
for pos,seq in s15.search_instances(test_seq):
	print pos,seq.tostring()

s16 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s16.add_instance(Seq("ATACATGAGGTT",s16.alphabet))
#test_seq=Seq(sequence, s16.alphabet)
for pos,seq in s16.search_instances(test_seq):
	print pos,seq.tostring()

s17 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s17.add_instance(Seq("TTGTATAAAAAT",s17.alphabet))
#test_seq=Seq(sequence, s17.alphabet)
for pos,seq in s17.search_instances(test_seq):
	print pos,seq.tostring()

s18 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s18.add_instance(Seq("GTGACCAAAGAG",s18.alphabet))
#test_seq=Seq(sequence, s18.alphabet)
for pos,seq in s18.search_instances(test_seq):
	print pos,seq.tostring()

s19 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s19.add_instance(Seq("ATCCGCATTCCG",s19.alphabet))
#test_seq=Seq(sequence, s19.alphabet)
for pos,seq in s19.search_instances(test_seq):
	print pos,seq.tostring()

s20 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s20.add_instance(Seq("GTAATAGGACTG",s20.alphabet))
#test_seq=Seq(sequence, s20.alphabet)
for pos,seq in s20.search_instances(test_seq):
	print pos,seq.tostring()

s21 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s21.add_instance(Seq("TACCCTGTGAGA",s21.alphabet))
#test_seq=Seq(sequence, s21.alphabet)
for pos,seq in s21.search_instances(test_seq):
	print pos,seq.tostring()

s22 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s22.add_instance(Seq("CGTTTTCTGCGT",s22.alphabet))
#test_seq=Seq(sequence, s22.alphabet)
for pos,seq in s22.search_instances(test_seq):
	print pos,seq.tostring()

#
# longer matches
#
s23 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s23.add_instance(Seq("TTACCACGATATTGGGCAGC",s23.alphabet))
#test_seq=Seq(sequence, s23.alphabet)
for pos,seq in s23.search_instances(test_seq):
	print pos,seq.tostring()

s24 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s24.add_instance(Seq("TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA",s24.alphabet))
#test_seq=Seq(sequence, s24.alphabet)
for pos,seq in s24.search_instances(test_seq):
	print pos,seq.tostring()

endtime = datetime.datetime.now( )
print endtime - starttime


#
# This is from BioPython
#
#

print "Biopyhton exact matches!"

from Bio.Seq import Seq

from Bio.Alphabet import IUPAC

starttime = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("TATAA",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)
for pos,seq in s1.search_instances(test_seq):
	print pos,seq.tostring()

s2 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s2.add_instance(Seq("GTTCGGCG",s2.alphabet))
#test_seq=Seq(sequence, s2.alphabet)
for pos,seq in s2.search_instances(test_seq):
	print pos,seq.tostring()

s3 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s3.add_instance(Seq("CAAATGCA",s3.alphabet))
#test_seq=Seq(sequence, s3.alphabet)
for pos,seq in s3.search_instances(test_seq):
	print pos,seq.tostring()

s4 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s4.add_instance(Seq("TGCCGCGC",s4.alphabet))
#test_seq=Seq(sequence, s4.alphabet)
for pos,seq in s4.search_instances(test_seq):
	print pos,seq.tostring()

s5 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s5.add_instance(Seq("TGGCGAAG",s5.alphabet))
#test_seq=Seq(sequence, s5.alphabet)
for pos,seq in s5.search_instances(test_seq):
	print pos,seq.tostring()

s6 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s6.add_instance(Seq("CCAACGTG",s6.alphabet))
#test_seq=Seq(sequence, s6.alphabet)
for pos,seq in s6.search_instances(test_seq):
	print pos,seq.tostring()

s7 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s7.add_instance(Seq("AATCGGGT",s7.alphabet))
#test_seq=Seq(sequence, s7.alphabet)
for pos,seq in s7.search_instances(test_seq):
	print pos,seq.tostring()

s8 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s8.add_instance(Seq("GTAATCAA",s8.alphabet))
#test_seq=Seq(sequence, s8.alphabet)
for pos,seq in s8.search_instances(test_seq):
	print pos,seq.tostring()

s9 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s9.add_instance(Seq("TATTTTTT",s9.alphabet))
#test_seq=Seq(sequence, s9.alphabet)
for pos,seq in s9.search_instances(test_seq):
	print pos,seq.tostring()

s10 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s10.add_instance(Seq("ATTATCCG",s10.alphabet))
#test_seq=Seq(sequence, s10.alphabet)
for pos,seq in s10.search_instances(test_seq):
	print pos,seq.tostring()

s11 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s11.add_instance(Seq("TTGTCTAA",s11.alphabet))
#test_seq=Seq(sequence, s11.alphabet)
for pos,seq in s11.search_instances(test_seq):
	print pos,seq.tostring()
#
# medium searches
#

s12 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s12.add_instance(Seq("TTTTTAAAAAAA",s12.alphabet))
#test_seq=Seq(sequence, s12.alphabet)
for pos,seq in s12.search_instances(test_seq):
	print pos,seq.tostring()

s13 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s13.add_instance(Seq("TTGCGGCCCGTG",s13.alphabet))
#test_seq=Seq(sequence, s13.alphabet)
for pos,seq in s13.search_instances(test_seq):
	print pos,seq.tostring()

s14 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s14.add_instance(Seq("ATCAGTGGGAAC",s14.alphabet))
#test_seq=Seq(sequence, s14.alphabet)
for pos,seq in s14.search_instances(test_seq):
	print pos,seq.tostring()

s15 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s15.add_instance(Seq("GGCGATATCAAC",s15.alphabet))
#test_seq=Seq(sequence, s15.alphabet)
for pos,seq in s15.search_instances(test_seq):
	print pos,seq.tostring()

s16 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s16.add_instance(Seq("ATACATGAGGTT",s16.alphabet))
#test_seq=Seq(sequence, s16.alphabet)
for pos,seq in s16.search_instances(test_seq):
	print pos,seq.tostring()

s17 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s17.add_instance(Seq("TTGTATAAAAAT",s17.alphabet))
#test_seq=Seq(sequence, s17.alphabet)
for pos,seq in s17.search_instances(test_seq):
	print pos,seq.tostring()

s18 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s18.add_instance(Seq("GTGACCAAAGAG",s18.alphabet))
#test_seq=Seq(sequence, s18.alphabet)
for pos,seq in s18.search_instances(test_seq):
	print pos,seq.tostring()

s19 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s19.add_instance(Seq("ATCCGCATTCCG",s19.alphabet))
#test_seq=Seq(sequence, s19.alphabet)
for pos,seq in s19.search_instances(test_seq):
	print pos,seq.tostring()

s20 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s20.add_instance(Seq("GTAATAGGACTG",s20.alphabet))
#test_seq=Seq(sequence, s20.alphabet)
for pos,seq in s20.search_instances(test_seq):
	print pos,seq.tostring()

s21 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s21.add_instance(Seq("TACCCTGTGAGA",s21.alphabet))
#test_seq=Seq(sequence, s21.alphabet)
for pos,seq in s21.search_instances(test_seq):
	print pos,seq.tostring()

s22 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s22.add_instance(Seq("CGTTTTCTGCGT",s22.alphabet))
#test_seq=Seq(sequence, s22.alphabet)
for pos,seq in s22.search_instances(test_seq):
	print pos,seq.tostring()

#
# longer matches
#
s23 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s23.add_instance(Seq("TTACCACGATATTGGGCAGC",s23.alphabet))
#test_seq=Seq(sequence, s23.alphabet)
for pos,seq in s23.search_instances(test_seq):
	print pos,seq.tostring()

s24 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s24.add_instance(Seq("TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA",s24.alphabet))
#test_seq=Seq(sequence, s24.alphabet)
for pos,seq in s24.search_instances(test_seq):
	print pos,seq.tostring()

endtime = datetime.datetime.now( )
print sequenceendtime - sequencestarttime
print endtime - starttime
