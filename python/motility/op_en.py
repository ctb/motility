def load(filename):
    """
    A function to load an op-en-style bndarray from a file.  Returns an
    array suitable for passing into motility.
    """

    s = open(filename)
    length = int(s.readline())
    
    arr = []
    for i in range(0, length):
        l = s.readline()
        (A, C, G, T) = l.split()
        (A, C, G, T) = map(float, (A, C, G, T))

        arr.append((A, C, G, T,))

    return arr
