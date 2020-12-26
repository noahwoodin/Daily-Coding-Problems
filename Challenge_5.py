# Coding Challenge #5 (Medium)

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    ca = lambda a, b: a
    return pair(ca)


def cdr(pair):
    cd = lambda a, b: b
    return pair(cd)


assert car(cons(1, 2)) == 1
assert cdr(cons(1, 2)) == 2
