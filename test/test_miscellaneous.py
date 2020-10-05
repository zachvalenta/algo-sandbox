from src.miscellaneous import (
    countdown,
    do_factorial,
    do_sum,
    find_positive_factors,
    fizz_buzz,
    rotate_array,
    set_cover,
)


def test_countdown():
    assert countdown(0) is None


def test_do_sum():
    assert do_sum(4) == 10


def test_do_factorial():
    do_factorial(4) == 24


def test_set_cover():
    states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"},
    }
    assert set_cover(states_needed=states, stations=stations) == [
        "kone",
        "ktwo",
        "kthree",
        "kfive",
    ]  # could be 2-5 as well [8.152]


def test_rotate_array():
    my_arr = [1, 2, 3, 4]
    assert list(rotate_array(my_arr)) == [4, 1, 2, 3]


def test_fizz_buzz():
    assert fizz_buzz(3) == "fizz"
    assert fizz_buzz(5) == "buzz"
    assert fizz_buzz(7) == 7


def test_find_positive_factors():
    assert find_positive_factors(16) == [1, 2, 4, 8, 16]
    assert find_positive_factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
