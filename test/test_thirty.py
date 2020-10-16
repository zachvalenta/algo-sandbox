from src.thirty import (
    all_eq_naive,
    all_eq_pythonic,
    all_unique,
    arithmetic_progression,
    upper_words_in_string,
)


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


def test_arithmetic_progression():
    assert arithmetic_progression(start=3, stop=21) == [3, 6, 9, 12, 15, 18, 21]
    assert arithmetic_progression(start=5, stop=25) == [5, 10, 15, 20, 25]
    assert arithmetic_progression(start=10, stop=50) == [10, 20, 30, 40, 50]


def test_uppercase():
    assert upper_words_in_string(txt="alice and bob") == "Alice And Bob"
    assert upper_words_in_string(txt="here's another one") == "Here's Another One"
