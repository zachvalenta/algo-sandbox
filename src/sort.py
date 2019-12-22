def quicksort(unsorted_list):

    # BASE
    if len(unsorted_list) < 2:
        return unsorted_list

    # SORT
    if len(unsorted_list) == 2:
        if unsorted_list[0] > unsorted_list[1]:
            tmp = unsorted_list[0]  # find more elegant impl
            unsorted_list[0] = unsorted_list[1]
            unsorted_list[1] = tmp
            return unsorted_list

    # PARTITION
    pivot = unsorted_list[len(unsorted_list) // 2]
    smaller = [x for x in unsorted_list if x < pivot]
    larger = [x for x in unsorted_list if x > pivot]
    first_half = quicksort(smaller)
    first_half.append(pivot)  # append and return new list in single go
    second_half = quicksort(larger)
    return first_half + second_half


def selection_sort(unsorted_list):
    """
    * 📙 32
    * 📈 O(n^2)
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
