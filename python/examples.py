#! /usr/bin/env python
import motility

print '\n---------------------------------\n'
##############################################################################

#
# example 1: use an IUPAC motif with and without mismatches.
#

motif = "AR"                           # R = A or G
seq = "ATCT"                           # sequence to search

### 0 mismatches

matches = motility.find_iupac(seq, motif) # search with zero mismatches

print "found %d match(es) to '%s' in '%s' with 0 mismatches:" \
      % (len(matches), motif, seq)

for (start, end, o, match) in matches:
    print '\t%d to %d in %d orientation; match is %s' % (start, end, o, match)

### 1 mismatch allowed

matches = motility.find_iupac(seq, motif, 1) # search with 1 mismatch

print "\nfound %d match(es) to '%s' in '%s' with 1 mismatch allowed:" \
      % (len(matches), motif, seq)

for (start, end, o, match) in matches:
    print '\t%d to %d in %d orientation; match is %s' % (start, end, o, match)

print '\n---------------------------------\n'
##############################################################################

#
# example 2: use a position weight matrix.
#

matrix = [ [ 1.0, 0.0, 0.5, 0.0, 0.0 ],    # A   or 1/2 G
           [ 2.0, 0.0, 0.0, 1.0, 0.0 ] ]   # 2 A or T

seq = "AACT"                           # sequence to search

pwm = motility.PWM(matrix)

### match max

threshold = 3
matches = pwm.find(seq, threshold) # search for best match (AA)

print "found %d match(es) to pwm in '%s:' at %f:" % (len(matches), seq,
                                                     threshold)

for (start, end, o, match) in matches:
    print '\t%d to %d in %d orientation; match is %s' % (start, end, o, match)

### match to *anything* good.

threshold = 1.5
matches = pwm.find(seq, threshold)

print "\nfound %d match(es) to pwm in '%s' at %f:" % (len(matches), seq,
                                                    threshold)

for (start, end, o, match) in matches:
    print '\t%d to %d in %d orientation; match is %s' % (start, end, o, match)

print '\n---------------------------------\n'
##############################################################################

#
# example 3: use an energy operator
#

matrix = [ [ 0.0, 1.0, 0.5, 1.0, 1.0 ],    # A   or 1/2 G
           [ 0.0, 1.0, 1.0, 0.0, 1.0 ] ]   # A or T

seq = "AACT"                           # sequence to search

operator = motility.EnergyOperator(matrix)

### match max

threshold = 0.0
matches = operator.find(seq, threshold) # search for AA

print "found %d match(es) to operator in '%s:' at %f:" % (len(matches), seq,
                                                          threshold)

for (start, end, o, match) in matches:
    print '\t%d to %d in %d orientation; match is %s' % (start, end, o, match)

### match to *anything* good.

threshold = .5
matches = operator.find(seq, threshold)

print "\nfound %d match(es) to matrix in '%s' at %f:" % (len(matches), seq,
                                                         threshold)

for (start, end, o, match) in matches:
    print '\t%d to %d in %d orientation; match is %s' % (start, end, o, match)

print '\n---------------------------------\n'

