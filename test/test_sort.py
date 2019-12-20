import src.sort as sort


def test_selection_sort():
    assert sort.selection_sort([47, 14, 50]) == [50, 47, 14]
