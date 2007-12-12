import motility
import threading

def do_motif_search(offset, fn, params):
    kw = dict(offset=offset)
    results = fn(*params, **kw)
#    results = [ (a + offset, b + offset, o, m) for (a,b,o,m) in results ]

    return results

class ThreadedMotifSearch(threading.Thread):
    def __init__(self, seq, motif, offset, fn, params):
        threading.Thread.__init__(self)
        self.fn = fn
        self.offset = offset
        self.params = [seq, motif] + list(params)
               
    def run(self):
        print 'RUNNING: offset is', self.offset
        self.results = do_motif_search(self.offset, self.fn, self.params)

        print len(self.results)

def threaded_search(n_threads, seq, motif, fn, *params):
    assert n_threads > 0
    
    seqlen = len(seq)

    chunksize = seqlen / n_threads
    if chunksize < len(motif):
        raise Exception

    threads = []
    for i in range(n_threads - 1):
        start = i*chunksize
        stop = start + chunksize + len(motif)
        chunk = seq[start:stop]
        t = ThreadedMotifSearch(chunk, motif, start, fn, params)
        threads.append(t)

    start = (i+1) * chunksize
    print '==>', start
    t = ThreadedMotifSearch(seq[start:], motif, start, fn, params)
    threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print 'done'

    results = []
    for t in threads:
        results += t.results

    return results

seq = open('50mb-random.fa').read().strip()

results = threaded_search(5, seq, 'AAAAGCTAGCT', motility.find_iupac)
print 'TOTAL', len(results)
