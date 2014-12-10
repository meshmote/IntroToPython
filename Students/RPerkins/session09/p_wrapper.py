__author__ = 'Robert W. Perkins'


class p_wrapper():

    def __init__(self, o_string):

        self.o_string = o_string

    def __call__(self, *args):
        return '<p> %s </p>' % args


class tag_wrapper():
    pass
