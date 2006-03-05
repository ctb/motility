#! /usr/bin/env python
import sys
sys.path.append('/u/t/dev/motility/python/build/lib.linux-i686-2.3/')
import motility

sys.path.append('/u/t/dev/slippy/lib')
import fasta

if len(sys.argv) != 3:
    sys.stderr.write('Usage:\n\t%s <motif> <FASTA file to search>\n' % (sys.argv[0],))
    sys.exit(0)

motif = sys.argv[1]
filename = sys.argv[2]

sys.stderr.write('searching file %s with motif %s\n' % (filename, motif,))

seq = fasta.load_single(filename)
results = motility.find_iupac(seq, motif)

for (start, end, orientation, match) in results:
    print 'MATCH: %d --> %d, orientation %d; match is %s' % (start, end,
                                                             orientation,
                                                             match,)

sys.exit(0)
