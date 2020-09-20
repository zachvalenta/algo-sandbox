from src.cake import mtg_merge


def test_mtg_merge():
    # other pairs (11, 15) (12, 15) (6, 11)
    assert mtg_merge(mtgs=[(7, 10), (3, 5)]) == [(3, 5), (7, 10)]
    assert mtg_merge(mtgs=[(7, 10), (3, 6)]) == [(3, 10)]
