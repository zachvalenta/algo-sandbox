from src.hacker_rank import (
    counting_valleys,
    jump_clouds,
    ransom_note,
    repeated_string,
    sock_merchant,
    sum_hourglass,
)


def test_ransom_note():
    assert (
        ransom_note(
            magazine="give me one grand today night", note="give one grand today"
        )
        is True
    )
    assert (
        ransom_note(
            magazine="two times three is not four", note="two times two is four"
        )
        is False
    )
    assert (
        ransom_note(
            magazine="ive got a lovely bunch of flower", note="ive got some coconuts"
        )
        is False
    )


def test_counting_valleys():
    """
    _/\_______
       \    /
        \/\/
    """
    assert counting_valleys(s="UDDDUDUU") == 1
    """
    __________
    \/\      /
       \  /\/
        \/
    """
    assert counting_valleys(s="DDUUDDUDUUUD") == 2
    """
         /\/\
        /    \
    _/\/______\
    """
    assert counting_valleys(s="UDUUUDUDDD") == 0
    """
    __________________
    \/\      /
       \  /\/
        \/
    """
    assert counting_valleys(s="DUDDDUUDUU") == 2


def test_jump_clouds():
    assert jump_clouds([0, 0, 0, 1, 0, 0]) == 3
    assert jump_clouds([0, 1, 0, 0, 0, 1, 0]) == 3
    assert jump_clouds([0, 0, 1, 0, 0, 1, 0]) == 4


def test_repeat_string():
    assert repeated_string(s="aba", n=10) == 7
    assert repeated_string(s="a", n=1000000000000) == 1000000000000
    assert repeated_string(s="aab", n=882787) == 588525


def test_sock_merchant():
    assert sock_merchant(ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3


def test_sum_hourglass():
    two_d1 = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    two_d2 = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 9, 2, -4, -4, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, -1, -2, -4, 0],
    ]
    two_d3 = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    two_d4 = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]
    assert sum_hourglass(two_d1) == 19
    assert sum_hourglass(two_d2) == 13
    assert sum_hourglass(two_d3) == 28
    assert sum_hourglass(two_d4) == -6
