import src.recursion as r


def test_countdown():
    assert r.countdown(0) is None


def test_do_sum():
    assert r.do_sum(4) == 10


def test_do_factorial():
    r.do_factorial(4) == 24
