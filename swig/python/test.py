import sys
import motility_ext

for i in motility_ext.find_iupac("ACGGT", "G", 0):
    print i

print '---'

matrix = ((0., 0., 1., 0., 0.,),)

for i in motility_ext.find_pwm("ACGTG", matrix, 1):
    print i

print '---'

matrix = ((1., 1., 0., 1., 1.,),)

for i in motility_ext.find_energy("ACGTG", matrix, 0):
    print i
