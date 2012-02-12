""" beat_breeder.util
"""
def shallow_flatten(l):
    return reduce(lambda x,y: (type(x) is list and x or [x])+(type(y) is list and y or [y]),l)

def flatten(x):
    if type(x) == list:
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def gcd(ints):
    def gcd_internal(a, b):
        a = abs(a)
        b = abs(b)
        while a:
                a, b = b%a, a
        return b

    return reduce(gcd_internal, ints)
