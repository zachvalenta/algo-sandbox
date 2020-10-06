###
# ARRAYS
###


def mtg_merge(mtgs):
    """
    https://www.interviewcake.com/question/python3/merging-ranges
    take list of meetings and merge into blocks when possible
    list of meetings not sorted but meeting start/end are
    """
    mtgs.sort()
    blocks = list()
    for ind, mtg in enumerate(mtgs):
        # initial block
        if ind == 0:
            blocks.append((mtg[0], mtg[1]))
            continue
        # DSL
        mtg_start = mtg[0]
        mtg_end = mtg[1]
        block_start = blocks[-1:][0][0]
        block_end = blocks[-1:][0][1]
        # logic
        if block_end >= mtg_start:
            if block_end >= mtg_end:
                blocks.pop()
                blocks.append((block_start, block_end))
            else:
                blocks.pop()
                blocks.append((block_start, mtg_end))
        else:
            blocks.append((mtg_start, mtg_end))
    return blocks


def reverse_out_of_place_imperative(qd):
    new_qd = []
    for i in reversed(qd):
        new_qd.append(i)
    return new_qd


def reverse_out_of_place_pythonic(qd):
    return qd[::-1]


def reverse_in_place_imperative(qd):
    if not qd:
        return qd
    start = 0
    end = len(qd) - 1
    for ind, el in enumerate(qd):
        if ind == len(qd) // 2:
            return qd
        qd[start], qd[end] = qd[end], qd[start]
        start += 1
        end -= 1


def reverse_in_place_pythonic(qd):
    qd.reverse()
    return qd
