from src.za import set_cover


def test_set_cover():
    states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"},
    }
    assert set_cover(states_needed=states, stations=stations) == [
        "kone",
        "ktwo",
        "kthree",
        "kfive",
    ]  # could be 2-5 as well [8.152]
