from collections import deque
import random


def simple():
    number_to_guess = random.randint(0, 99)
    accumulated_guesses = 0
    for guess in range(0, 100):
        accumulated_guesses = accumulated_guesses + 1
        if guess == number_to_guess:
            return accumulated_guesses


def binary(query, sorted_list):
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
    queue = deque(graph['root'])
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
