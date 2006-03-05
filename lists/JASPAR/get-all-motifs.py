#! /usr/bin/env python
import sys, urllib

DOWNLOAD_URL="http://jaspar.cgb.ki.se/DOWNLOAD/MatrixDir/%s.pfm"

list = open(sys.argv[1]).readlines()
list = [ i.split()[0] for i in list ]

for name in list:
    print 'getting', name
    url = DOWNLOAD_URL % (name,)
    f = urllib.urlopen(url)
    matrix = f.read()

    out = open('data/%s.pfm' % (name,), 'w')
    out.write(matrix)
    out.close()

print 'got %d total' % (len(list),)
