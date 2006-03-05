"""
Utilities for dealing with the JASPAR motif collection.
"""

import os.path
from objects import PWM

def load(list_file, matrix_dir):
    """
    Load all of the matrices in list_file from matrix_dir.  Return a
    dictionary of PWM objects.
    """

    list = open(list_file).readlines()
    list = [ i.split() for i in list ]
    list = [ (i[0], i[2],) for i in list ]

    # list now contains matrix file, name.

    d = {}
    for (matrix_file, name) in list:
        filename = '%s.pfm' % (matrix_file,)
        matrix_file = os.path.join(matrix_dir, filename)
        d[name] = PWM(load_matrix(matrix_file))

    return d


def load_matrix(matrix_file):
    """
    Load an individual matrix into a motility-compatible format.
    """
    f = open(matrix_file)
    l = f.readlines()

    # break up on whitespace
    l = [ i.split() for i in l if len(i.strip()) ]

    l = [ map(int, i) for i in l ]

    # double-check the length of the lines
    assert len(l) == 4

    lens = map(len, l)
    assert min(lens) == max(lens)
    site_len = min(lens)

    # ok, now transpose the matrix and add a 0 for 'N's.
    mat = []
    for i in range(0, site_len):
        A = l[0][i]
        C = l[1][i]
        G = l[2][i]
        T = l[3][i]
        N = 0

        mat.append((A, C, G, T, N,))

    return mat
