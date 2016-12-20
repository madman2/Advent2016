# Day 11: Radioisotope Thermoelectric Generators

from itertools import combinations_with_replacement
from itertools import combinations
from collections import defaultdict

def main():
    start = ((1, 1), (1, 2), (1, 2), (3, 3), (3, 3))
    end = ((4, 4), (4, 4), (4, 4), (4, 4), (4, 4))
    solve(start, end, 5)

def solve(start, end, n):
    floors = [i for i in range(1, 5)]
    c_pairs = [(i, j) for i in floors for j in floors]
    c_states = list(combinations_with_replacement(c_pairs, n))

    valid_states = []
    for state in c_states:
        unpaired_micro = set()
        generators = set()
        for pair in state:
            generators.add(pair[0])
            if pair[0] != pair[1]:
                unpaired_micro.add(pair[1])
        if generators.isdisjoint(unpaired_micro):
            valid_states.append(state)

    d = {key: set() for key in valid_states}
    edges = dict()
    for nodes in combinations(valid_states, 2):
        elevator = is_connected(nodes[0], nodes[1])
        if elevator:
            d[nodes[0]].add(nodes[1])
            d[nodes[1]].add(nodes[0])
            edges[(nodes[0], nodes[1])] = elevator
            edges[(nodes[1], nodes[0])] = elevator[::-1]

def is_connected(node1, node2):
    elevator = (0, 0)
    item_count = 0
    for pair1, pair2 in zip(node1, node2):
        for floor1, floor2 in zip(pair1, pair2):
            diff = abs(floor1 - floor2)
            if diff > 1:
                return None
            if diff == 1:
                if item_count > 0:
                    if item_count > 1:
                        return None
                    if elevator != (floor1, floor2):
                        return None
                    item_count += 1
                else:
                    elevator = (floor1, floor2)
                    item_count += 1

    return elevator

if __name__ == "__main__":
    main()