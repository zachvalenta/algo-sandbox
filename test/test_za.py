from src.za import container_ship, find_longest_substring, word_count


def test_container_ship():
    consumption = [3, 5, 2, 1]
    timestamps = [0, 3, 5, 8]
    assert container_ship(cons=consumption, stamps=timestamps) == 25


def test_find_longest_substring():
    assert find_longest_substring("") == 0
    assert find_longest_substring("bbbb") == 1
    assert find_longest_substring("abcabcbb") == 3
    assert find_longest_substring("pwwkew") == 3


def test_word_count():
    text = "wipe the sweat off my dome, spit the phlegm in the street"
    assert word_count(text) == "the"
