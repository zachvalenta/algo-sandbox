from collections import deque


def rotate_array(arr):
    dq = deque(arr)
    dq.rotate(1)
    return dq


def reverse_array_imperative(arr):
    holder = []
    for i in reversed(arr):
        holder.append(i)
    return holder


def fizz_buzz(num):
    if num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num


def set_cover(states_needed, stations):
    states_covered = set()
    stations_chosen = list()

    # could rm from states_needed when adding to states_acquired
    # and stop iteration when states_needed is empty/falsy i.e. `when states_needed:`
    while states_covered != states_needed:

        station_w_most_uncovered_states = None
        states_from_station_w_most = set()

        for station, states in stations.items():
            uncovered_from_current_station = states - states_covered
            if len(uncovered_from_current_station) > len(states_from_station_w_most):
                station_w_most_uncovered_states = station
                states_from_station_w_most = uncovered_from_current_station

        states_covered.update(states_from_station_w_most)
        stations_chosen.append(station_w_most_uncovered_states)

    return stations_chosen


def find_positive_factors(num):
    factors = list()
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


# recursion


def countdown(arg):
    """
    * pg. 41
    """
    print(arg)
    return None if arg == 0 else countdown(arg - 1)


def do_sum(arg):
    if arg == 0:
        return arg
    else:
        return arg + do_sum(arg - 1)


def do_factorial(arg):
    """
    * pg. 45
    """
    if arg == 1:
        return arg
    else:
        return arg * do_factorial(arg - 1)
