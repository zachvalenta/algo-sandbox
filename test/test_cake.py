from src.cake import mtg_merge


def test_mtg_merge():
    control = (7, 10)
    # link miss to control minorant
    assert mtg_merge(mtgs=[(control), (3, 5)]) == [(3, 5), (control)]
    # link to control minorant
    assert mtg_merge(mtgs=[(control), (3, 6)]) == [(3, 10)]
    # link to control majorant
    assert mtg_merge(mtgs=[(control), (11, 15)]) == [(7, 15)]
    # link miss to control majorant
    assert mtg_merge(mtgs=[(control), (12, 15)]) == [(control), (12, 15)]
