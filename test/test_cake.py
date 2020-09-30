from src.cake import mtg_merge


def test_mtg_merge():
    # maj > min
    assert mtg_merge(mtgs=[(1, 3), (2, 4)]) == [(1, 4)]
    # maj = min
    assert mtg_merge(mtgs=[(5, 6), (6, 8)]) == [(5, 8)]
    # maj > min & maj > maj
    assert mtg_merge(mtgs=[(1, 8), (2, 5)]) == [(1, 8)]
    # append
    assert mtg_merge(mtgs=[(1, 3), (4, 8)]) == [(1, 3), (4, 8)]
    # multi
    assert mtg_merge(mtgs=[(1, 4), (2, 5), (5, 8)]) == [(1, 8)]
    assert mtg_merge(mtgs=[(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)]) == [(1, 12)]
    assert mtg_merge(mtgs=[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [
        (0, 1),
        (3, 8),
        (9, 12),
    ]
