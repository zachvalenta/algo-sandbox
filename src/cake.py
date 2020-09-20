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
        block_start = blocks[0][0]
        block_end = blocks[0][1]
        # conditions
        linkable = block_end + 1 == mtg_start
        # logic
        if linkable:
            blocks[0] = (block_start, mtg_end)
        else:
            blocks.append((mtg_start, mtg_end))
    return blocks
