from src.thirty import all_eq_naive, all_eq_pythonic, all_unique


def test_all_eq():
    eq = [1, 1, 1]
    un_eq = [1, 2, 3]
    assert all_eq_naive(qd=eq) is True
    assert all_eq_pythonic(qd=eq) is True
    assert all_eq_naive(qd=un_eq) is False
    assert all_eq_pythonic(qd=un_eq) is False


def test_all_unique():
    unique = [1, 2, 3]
    dupes = [1, 2, 1]
    assert all_unique(qd=unique) is True
    assert all_unique(qd=dupes) is False
