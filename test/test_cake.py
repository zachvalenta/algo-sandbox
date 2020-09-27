from src.cake import mtg_merge


def test_mtg_merge():
    control = (7, 10)

    # MAJORANT TO MINORANT
    # link
    assert mtg_merge(mtgs=[control, (3, 6)]) == [(3, 10)]
    # link miss
    assert mtg_merge(mtgs=[control, (12, 15)]) == [control, (12, 15)]

    # MINORANT TO MINORANT
    # link
    assert mtg_merge(mtgs=[control, (6, 9)]) == [(6, 10)]
    assert mtg_merge(mtgs=[(1, 3), (2, 4)]) == [(1, 4)]  # their test case
    assert mtg_merge(mtgs=[(5, 6), (6, 8)]) == [(5, 8)]  # their test case
    assert mtg_merge(mtgs=[(1, 8), (2, 5)]) == [(1, 8)]  # their test case
    # link miss
    assert mtg_merge(mtgs=[control, (5, 8)]) == [(5, 8), (7, 10)]

    # MAJORANT TO MAJORANT
    # link
    assert mtg_merge(mtgs=[control, (8, 11)]) == [(7, 11)]
    # link miss
    assert mtg_merge(mtgs=[control, (8, 10)]) == [(7, 10)]

    # DOUBLE (MIN-MIN + MAJ-MAJ)
    assert mtg_merge(mtgs=[control, (3, 11)]) == [(3, 11)]
