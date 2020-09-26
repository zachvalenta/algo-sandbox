from src.cake import mtg_merge


def test_mtg_merge():
    control = (7, 10)

    # MAJORANT TO MINORANT
    # link
    assert mtg_merge(mtgs=[control, (3, 6)]) == [(3, 10)]
    assert mtg_merge(mtgs=[control, (11, 15)]) == [(7, 15)]
    # link miss
    assert mtg_merge(mtgs=[control, (3, 5)]) == [(3, 5), control]
    assert mtg_merge(mtgs=[control, (12, 15)]) == [control, (12, 15)]

    # MINORANT TO MINORANT
    # link
    assert mtg_merge(mtgs=[control, (6, 9)]) == [(6, 10)]

    assert mtg_merge(mtgs=[control, (3, 11)]) == [(3, 11)]

    # their unit tests
    assert mtg_merge(mtgs=[(1, 3), (2, 4)]) == [(1, 4)]
    assert mtg_merge(mtgs=[(5, 6), (6, 8)]) == [(5, 8)]
    assert mtg_merge(mtgs=[(1, 8), (2, 5)]) == [(1, 8)]
