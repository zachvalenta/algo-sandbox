import src.sort as sort


def test_quicksort():
    # base
    assert sort.quicksort(unsorted_list=[]) == []
    assert sort.quicksort(unsorted_list=[42]) == [42]
    # recursive
    assert sort.quicksort(unsorted_list=[42, 13]) == [13, 42]
    assert sort.quicksort(unsorted_list=[99, 13, 42]) == [13, 42, 99]
    assert sort.quicksort(unsorted_list=[99, 13, 100, 42]) == [13, 42, 99, 100]
    assert sort.quicksort(unsorted_list=[99, 13, 100, 42, 7]) == [7, 13, 42, 99, 100]


def test_selection_sort():
    assert sort.selection_sort([47, 14, 50]) == [50, 47, 14]
