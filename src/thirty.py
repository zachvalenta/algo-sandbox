def all_eq_naive(qd):
    for el in qd:
        if el != qd[0]:
            return False
    return True


def all_eq_pythonic(qd):
    """
    https://www.30secondsofcode.org/python/s/all-equal
    """
    return len(set(qd)) == 1
