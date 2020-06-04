from src.za import set_cover, countdown, do_factorial, do_sum, rotate_array


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
