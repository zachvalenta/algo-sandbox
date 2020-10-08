from collections import deque
import random


def simple():
    """
    🛠 look around in the attic
    📙 1.5
    📈 O(n)
    💡 "is it this one?" all the way through
    """
    number_to_guess = random.randint(0, 99)
    accumulated_guesses = 0
    for guess in range(0, 100):
        accumulated_guesses = accumulated_guesses + 1
        if guess == number_to_guess:
            return accumulated_guesses


def binary(query, sorted_list):
    """
    📙 1.6-8, 11.205
    📈 vs BST: ❌ slower for mutative ✅ O(log n) worst case, random access
    💡 needs sorted array, track low/high indices and derive middle index to halve list
    """
    low_index = 0
    high_index = len(sorted_list) - 1
    while low_index <= high_index:
        mid = (high_index + low_index) // 2
        if sorted_list[mid] == query:
            return f"found {query}"
        elif sorted_list[mid] > query:
            high_index = mid - 1
        else:
            low_index = mid + 1
    return f"could not find {query}"


def bfs(graph, condition):
    """
    🛠 shortest path through unweighted graph
    📙 6.110
    📈 O(n) where n is number of edges
    💡 take root K and handle each V (exit if yes, use V as K and enque its V)
    """
    queue = deque(graph["root"])
    while queue:
        current = queue.popleft()
        if current is condition:
            return True
        else:
            try:
                queue += graph[current]
            except KeyError:
                pass
    return False


def get_initial_paths(graph):
    paths = {}
    for k in graph["root"].keys():
        paths[k] = "root"
    paths["terminus"] = None
    return paths


def get_initial_path_weights(graph):
    path_weights = {}
    for k in graph.keys():
        if k != "root" and k != "terminus":
            path_weights[k] = graph["root"][k]
    path_weights["terminus"] = float("inf")
    return path_weights


def get_node_w_lightest_path(path_weights, processed_nodes):
    lightest_path = float("inf")
    node_w_lightest_path = None
    for node, weight in path_weights.items():
        if weight < lightest_path and node not in processed_nodes:
            lightest_path = weight
            node_w_lightest_path = node
    return node_w_lightest_path, lightest_path


def dijkstra(graph):
    """
    🛠 lightest path (weighted graph)
    📙 7.116
    📈 O(E log V) where E = edges and V = vertices https://stackoverflow.com/a/26548129
    💡 can't deal w/ negative weights [7.129]
    """

    # get starting values
    paths = get_initial_paths(graph)
    path_weights = get_initial_path_weights(graph)
    processed_nodes = []

    # is current node a lighter path to any of its neighbors
    # than the paths we already know about?
    # e.g. first iteration, is B a faster path to A than the root?
    node, pw = get_node_w_lightest_path(path_weights, processed_nodes)
    while graph[node] is not None:  # everything before terminus
        neighbors = graph[node]
        for nnode, nnode_pw in neighbors.items():
            pw_to_nnode = pw + nnode_pw
            if path_weights[nnode] > pw_to_nnode:
                path_weights[nnode] = pw_to_nnode
                paths[nnode] = node
        processed_nodes.append(node)
        node, pw = get_node_w_lightest_path(path_weights, processed_nodes)
    return path_weights


def engine(query, pages):
    results = list()
    for page in pages:
        if page.find(query) != -1:
            results.append(page)
    return results
