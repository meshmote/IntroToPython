__author__ = 'Robert W. Perkins'

import time

# with Timer as t:
# [x^2 for x in range(10000000))
# t.elapsed

class Timer(object):
    def __enter__(self):
        print "in __enter__"
        self.start = time.time()
        return self

    def __exit__(self, err_type, err_val, errc_trc):
        print "in __exit__"
        self.elapsed = time.time() - self.start
        print "run took %f seconds"%self.elapsed
        print err_type, err_val, errc_trc
        if issubclass(err_type, RuntimeError):
            print "this is a RuntimError"
            return True
        else:
            print "something else"
            return False