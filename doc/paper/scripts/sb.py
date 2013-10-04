#!/usr/bin/env python

# Biopython sb.py.

import datetime
import Bio

from Bio import Motif

#sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
#sequenceendtime = datetime.datetime.now( )

#
# This is from BioPython
#
#

from Bio.Seq import Seq

from Bio.Alphabet import IUPAC

outputfile = open("OUTPUT/sb.out", "w", 1)


starttimetata = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("TATAA",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)
for pos,seq in s1.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

s1r = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1r.add_instance(Seq("AATAT",s1r.alphabet))
test_seq=Seq(sequence, s1r.alphabet)
for pos,seq in s1r.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s1c = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s1c.add_instance(Seq("ATATT",s1r.alphabet))
#test_seq=Seq(sequence, s1c.alphabet)
#for pos,seq in s1c.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

#s1rc = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s1rc.add_instance(Seq("TTATA",s1rc.alphabet))
#test_seq=Seq(sequence, s1rc.alphabet)
#for pos,seq in s1rc.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

endtimetata = datetime.datetime.now( )
starttimesmall = datetime.datetime.now( )

s2 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s2.add_instance(Seq("GTTCGGCG",s2.alphabet))
for pos,seq in s2.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s2c = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s2c.add_instance(Seq("CAAGCCGC",s2c.alphabet))
#for pos,seq in s2c.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

s2r = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s2r.add_instance(Seq("GCGGCTTG",s2r.alphabet))
for pos,seq in s2r.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s2rc = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s2rc.add_instance(Seq("CGCCGAAC",s2rc.alphabet))
#for pos,seq in s2rc.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

endtimesmall = datetime.datetime.now( )
starttimemedium = datetime.datetime.now( )

s12 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s12.add_instance(Seq("TTTTTAAAAAAA",s12.alphabet))
for pos,seq in s12.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s12c = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s12c.add_instance(Seq("AAAAATTTTTTT",s12c.alphabet))
#for pos,seq in s12c.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

#s12r = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s12r.add_instance(Seq("TTTTTTTAAAAA",s12r.alphabet))
#for pos,seq in s12r.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

s12rc = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s12rc.add_instance(Seq("AAAAAAATTTTT",s12rc.alphabet))
for pos,seq in s12rc.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

endtimemedium = datetime.datetime.now( )
starttimelarge = datetime.datetime.now( )
#
# longer matches
#
s23 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s23.add_instance(Seq("TTACCACGATATTGGGCAGC",s23.alphabet))
for pos,seq in s23.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s23c = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s23c.add_instance(Seq("AATGGTGCTATAACCCGTCG",s23c.alphabet))
#for pos,seq in s23c.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

s23r = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s23r.add_instance(Seq("CGACGGGTTATAGCACCATT",s23r.alphabet))
for pos,seq in s23r.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s23rc = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s23rc.add_instance(Seq("GCTGCCCAATATCGTGGTAA",s23rc.alphabet))
#for pos,seq in s23rc.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

endtimelarge = datetime.datetime.now( )
starttimeverylarge = datetime.datetime.now( )

s24 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s24.add_instance(Seq("TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA",s24.alphabet))
for pos,seq in s24.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s24c = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s24c.add_instance(Seq("CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT",s24c.alphabet))
#for pos,seq in s24c.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

s24r = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s24r.add_instance(Seq("ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT",s24r.alphabet))
for pos,seq in s24r.search_instances(test_seq):
	print >> outputfile,  pos,seq.tostring()

#s24rc = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#s24rc.add_instance(Seq("TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA",s24rc.alphabet))
#for pos,seq in s24rc.search_instances(test_seq):
	#print >> outputfile,  pos,seq.tostring()

endtimeverylarge = datetime.datetime.now( )

timefile = open("OUTPUT/sb.time", "w", 1)

print >> timefile,  "Biopython exact matching times"
print >> timefile,  "TATA match time: ", endtimetata - starttimetata
print >> timefile,  "small sequence time: ", endtimesmall - starttimesmall
print >> timefile,  "medium sequence time: ", endtimemedium - starttimemedium
print >> timefile,  "large sequence time: ", endtimelarge - starttimelarge
print >> timefile,  "very large sequence time: ", endtimeverylarge - starttimeverylarge
