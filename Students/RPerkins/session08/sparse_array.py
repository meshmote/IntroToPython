__author__ = 'Robert W. Perkins'


class SparseArray(object):
    def __init__(self, iterable):
        #   self.s_array = {i: iterable[i] for i in iterable}
        self.values = {}
        self.length = len(iterable)
        for i, val in enumerate(iterable):
            if val:
                self.values[i] = val

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError("sparse array index out of range")
        else:
            return self.values.get(index, 0)

    def __len__(self):
        return self.length