def set_cover(states_needed, stations):
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"},
    }
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
