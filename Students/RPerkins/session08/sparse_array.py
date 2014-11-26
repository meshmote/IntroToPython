__author__ = 'Robert W. Perkins'


class SparseArray(object):
    def __init__(self, in_sequence):
        self.s_array = {i: in_sequence[i] for i in in_sequence}

    def __call__(self, x):

