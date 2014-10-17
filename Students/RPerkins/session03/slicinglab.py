def first_last(k):
	return k[-1] + k[1:-1] + k[0]


def eo_out(k):
	return k[0:13:2]


def eo_middle(k):
    return  k[4:-4:2]


def revstring(k):
    return k[::-1]


def midlasfir(k):
    chunk = len(k) // 3
    # this might work if the mod is added back to one of the chunks
    return k[chunk:-chunk] + k[-chunk:] + k[:chunk-1]



# Testing Block
if __name__ == "__main__":
    assert first_last('This is a test') == "this is a tesT"
    assert eo_out('This is a test') == "Ti sats"
    assert eo_middle('This is a test') == ' sa'
    assert revstring('This is a test') == 'tset a si sihT'
    assert midlasfir('This is a test') == ' is testThis'