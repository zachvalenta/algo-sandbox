from collections import Counter


def container_ship(cons, stamps):
    """
    consumption = [3, 5, 2, 1]
    timestamps = [0, 3, 5, 8]

    0 to 3 = 3 hours * 3 = 9 tons consumed
    3 to 5 = 2 hours * 6 = 10 tons consumed
    5 to 8 = 3 hours * 2 = 6 tons consumed

    25 tons total
    """
    total_cost = 0
    for x, y in zip(cons, stamps):
        next_i = stamps.index(y) + 1
        if next_i <= len(stamps) - 1:
            next_val = stamps[next_i]
            elapsed_time = next_val - y
            current_cost = elapsed_time * x
            total_cost += current_cost
    return total_cost


def common_substring(s1, s2):
    for x in s1:
        if s2.find(x) > -1:
            return "YES"
    return "NO"


def find_longest_substring(query):
    """
    find length of longest substring w/out repeating char

    further cases ⬇️

    assert scaffold('a') == 1
    assert scaffold('abcdbefghi') == ?
    """
    current = ""
    longest = 0
    for i, v in enumerate(query):
        if i == 0:
            longest = len(current)
            current += v
        else:
            if v in current and len(current) > longest:
                longest = len(current)
                current = v
            elif v in current:
                current = ""
            else:
                current += v
    return longest


def word_count(text):
    return Counter(text.split()).most_common()[0][0]


def count_pairs(nums, target):
    """
    count pairs in `nums` summing to `target`
    1 element can be in n pairs
    e.g. numbers = [4, 2, 1, 2] target = 6
    4 pairs w/ both 2s
    """
    pair_count = 0
    for ind, val in enumerate(nums):
        for sub_val in nums[ind + 1 :]:
            if val + sub_val == target:
                pair_count += 1
    return pair_count
