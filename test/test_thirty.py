from src.thirty import all_eq_naive, all_eq_pythonic


def test_all_eq():
    eq = [1, 1, 1]
    un_eq = [1, 2, 3]
    assert all_eq_naive(qd=eq) is True
    assert all_eq_pythonic(qd=eq) is True
    assert all_eq_naive(qd=un_eq) is False
    assert all_eq_pythonic(qd=un_eq) is False
