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
