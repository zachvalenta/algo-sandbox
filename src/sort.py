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
