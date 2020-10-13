def quicksort_zjv(qd):
    """
    ref: Bhargava 4.65
    runtime: O (n log n)
    strat: D&C via partition
    """
    # BASE
    if len(qd) < 2:
        return qd

    # SORT
    if len(qd) == 2:
        if qd[0] > qd[1]:
            qd[0], qd[1] = qd[1], qd[0]
            return qd

    # PARTITION
    pivot = qd[len(qd) // 2]
    smaller = [x for x in qd if x < pivot]
    larger = [x for x in qd if x > pivot]
    # RECURSION
    first_half = quicksort_zjv(smaller)
    first_half.append(pivot)
    second_half = quicksort_zjv(larger)
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
