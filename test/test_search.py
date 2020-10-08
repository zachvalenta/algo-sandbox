from src.search import simple, binary, bfs, dijkstra, engine


def test_simple():
    assert simple() <= 100


def test_binary_happy():
    query = 42
    list_happy = [2, 13, 24, 35, 42, 57, 68, 79]
    assert binary(query, list_happy) == "found 42"


def test_binary_sad():
    query = 42
    list_unhappy = [2, 13, 24, 35, 46, 57, 68, 79]
    assert binary(query, list_unhappy) == "could not find 42"


def test_bfs():
    network = dict()
    network["root"] = ["amber", "sean", "jack"]
    network["amber"] = ["joe"]
    network["jack"] = ["shuja", "garrett"]
    network["shuja"] = ["trotsky"]
    assert bfs(network, "trotsky") is True
    assert bfs(network, "bob") is False


def test_dijkstra():
    # nodes
    graph = {}
    graph["root"] = {}
    graph["a"] = {}
    graph["b"] = {}
    graph["terminus"] = None

    # edges
    graph["root"]["a"] = 6
    graph["root"]["b"] = 2
    graph["a"]["terminus"] = 1
    graph["b"]["a"] = 3
    graph["b"]["terminus"] = 5

    # TODO rf to return path/path weight to terminus
    """
    paths  # {'a': 'b', 'b': 'root', 'terminus': 'a'}
    paths['terminus']  # 'a'
    paths['a']  # 'b'
    paths['b']  # 'root'
    """
    assert dijkstra(graph) == {"a": 5, "b": 2, "terminus": 6}


def test_engine():
    page_one = "hi there"
    page_two = "hi you"
    page_three = "aloha"
    assert engine(query="hi", pages=[page_one, page_two, page_three]) == [
        page_one,
        page_two,
    ]
