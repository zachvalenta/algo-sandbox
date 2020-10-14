def quicksort(qd):
    """
    ref: Bhargava 4.65
    strat: D&C via partition
    space: O (n log n)
    time: O (n)
    notes: Bhargava's impl does diff concat
    """
    # BASE
    if len(qd) < 2:
        return qd

    # PARTITION
    pivot = qd[len(qd) // 2]
    # SORT
    smaller = [x for x in qd if x < pivot]
    larger = [x for x in qd if x > pivot]
    # RECURSE
    first_half = quicksort(smaller)
    first_half.append(pivot)
    second_half = quicksort(larger)
    return first_half + second_half


def selection_sort(unsorted_list):
    """
    📙 2.32
    📈 O(n^2)
    💡 iterate, helper function grabs high value and
    add to return list, rm from input list
    """
    unsorted_list_len = len(unsorted_list)
    sorted_list = []
    for _ in range(unsorted_list_len):
        high = find_high_val(unsorted_list)
        sorted_list.append(high)
        unsorted_list.remove(high)
    return sorted_list


def find_high_val(unsorted_at_time):
    high = 0
    for ind, val in enumerate(unsorted_at_time):
        if unsorted_at_time[ind] > high:
            high = val
    return high
