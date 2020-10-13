from src.sort import selection_sort, quicksort_adit, quicksort_zjv


def test_quicksort():
    # base
    assert quicksort_zjv(qd=[]) == []
    assert quicksort_zjv(qd=[42]) == [42]
    # recursive
    assert quicksort_zjv(qd=[42, 13]) == [13, 42]
    assert quicksort_zjv(qd=[99, 13, 42]) == [13, 42, 99]
    assert quicksort_zjv(qd=[99, 13, 100, 42]) == [13, 42, 99, 100]
    assert quicksort_zjv(qd=[99, 13, 100, 42, 7]) == [7, 13, 42, 99, 100]


def test_selection_sort():
    assert selection_sort([47, 14, 50]) == [50, 47, 14]
