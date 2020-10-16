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


def all_unique(qd):
    return len(set(qd)) == len(qd)


def arithmetic_progression(start, stop):
    qd = list()
    for el in range(start, stop + start, start):
        qd.append(el)
    return qd


def upper_words_in_string(txt):
    qd = list()
    for ind, el in enumerate(txt.split()):
        qd.append(el[0].upper() + el[1:])
    return " ".join(qd)
