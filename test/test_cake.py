from src.cake import mtg_merge


def test_mtg_merge():
    control = (7, 10)
    # majorant to minorant
    assert mtg_merge(mtgs=[control, (3, 6)]) == [(3, 10)]
    # append
    assert mtg_merge(mtgs=[control, (12, 15)]) == [control, (12, 15)]
    # block absorbs
    assert mtg_merge(mtgs=[control, (3, 11)]) == [(3, 11)]
    # minorant to minorant
    assert mtg_merge(mtgs=[control, (6, 9)]) == [(6, 10)]
    assert mtg_merge(mtgs=[(1, 3), (2, 4)]) == [(1, 4)]  # IC test case
    assert mtg_merge(mtgs=[(1, 8), (2, 5)]) == [(1, 8)]  # IC test case
    assert mtg_merge(mtgs=[control, (8, 11)]) == [(7, 11)]
    assert mtg_merge(mtgs=[control, (8, 10)]) == [(7, 10)]
    assert mtg_merge(mtgs=[(1, 4), (2, 5), (5, 8)]) == [(1, 8)]  # IC test case
