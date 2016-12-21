# Day 11: Radioisotope Thermoelectric Generators

from itertools import combinations_with_replacement
from itertools import permutations
from collections import defaultdict
import heapq

def main():
    # start = ((1, 1), (1, 1), (1, 1), (1, 2), (1, 2), (3, 3), (3, 3))
    # end = ((4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4))
    start = ((1, 1), (1, 2), (1, 2), (3, 3), (3, 3))
    end = ((4, 4), (4, 4), (4, 4), (4, 4), (4, 4))
    solve(start, end, len(start))

# Builds a graph where each vertex is a valid state, and the edges
# are tuples describing the elevator motion between those two states.
# A state is made up of tuples representing the pairs of items and
# which floors they are on
def solve(start, end, n):
    floors = [i for i in range(1, 5)]
    c_pairs = [(i, j) for i in floors for j in floors]
    c_states = list(combinations_with_replacement(c_pairs, n))

    valid_elevator_paths = build_elevator_paths(n)

    adj_dict = defaultdict(set)
    edges = dict()
    for state in c_states:
        if is_valid_state(state):
            for elevator_path, adj in get_adjacent_states(state, valid_elevator_paths):
                if is_valid_state(adj):
                    adj_dict[state].add(adj)
                    edges[state, adj] = elevator_path

    min_cost = dijkstra(adj_dict, edges, start, end)
    print(min_cost)

# Returns the shortest path from s to t
def dijkstra(adj, edges, s, t):
    Q = []
    d = {s: 0}
    Qd = {}
    visited_set = set([s])
    curr_elevator_floor = 1

    for v in adj[s]:
        if edges[s, v][0] == curr_elevator_floor:
            next_elevator_floor = edges[s, v][1]
            d[v, next_elevator_floor] = 1
            item = [d[v, next_elevator_floor], next_elevator_floor, v]
            heapq.heappush(Q, item)
            Qd[v] = item

    while Q:
        curr_path_length, curr_elevator_floor, u = heapq.heappop(Q)
        if u not in visited_set:
            visited_set.add((u, curr_elevator_floor))
            if u == t:
                return curr_path_length
            for v in adj[u]:
                if edges[(u, v)][0] == curr_elevator_floor:
                    next_elevator_floor = edges[(u, v)][1]
                    if d.get((v, next_elevator_floor)):
                        if d[v, next_elevator_floor] > 1 + curr_path_length:
                            d[v, next_elevator_floor] = 1 + curr_path_length
                            Qd[v, next_elevator_floor][0] = d[v, next_elevator_floor]
                            Qd[v, next_elevator_floor][1] = next_elevator_floor
                    else:
                        d[v, next_elevator_floor] = 1 + curr_path_length
                        item = [d[v, next_elevator_floor], next_elevator_floor, v]
                        heapq.heappush(Q, item)
                        Qd[v, next_elevator_floor] = item

    return None

# Returns the validity of a given state
def is_valid_state(state):
    unpaired_micro_floors = set()
    gen_floors = set()
    for gen_floor, micro_floor in state:
        if gen_floor > 4 or gen_floor < 1 or micro_floor > 4 or micro_floor < 1:
            return False
        gen_floors.add(gen_floor)
        if micro_floor != gen_floor:
            unpaired_micro_floors.add(micro_floor)
    return gen_floors.isdisjoint(unpaired_micro_floors)

# This returns a list of all the states theoretically accessible from a given state,
# irregardless of whether or not the new state is within the floor bounds [1, 4]
def get_adjacent_states(state, elevator_paths):
    for path in elevator_paths:
        for i in (-1, 1):
            result = []
            elevator_start = 0
            for pair, diff in zip(state, path):
                if diff[0] == 1 and diff[1] == 1:
                    if pair[0] != pair[1]:
                        break
                    elevator_start = pair[0]
                elif diff[0] == 1:
                    if elevator_start > 0:
                        if pair[0] != elevator_start:
                            break
                    else:
                        elevator_start = pair[0]
                elif diff[1] == 1:
                    if elevator_start > 0:
                        if pair[1] != elevator_start:
                            break
                    else:
                        elevator_start = pair[1]
                result.append((pair[0] + i * diff[0], pair[1] + i * diff[1]))
            if len(result) == len(state):
                yield ((elevator_start, elevator_start + i), tuple(sorted(result)))

# This builds all the possible elevator paths. These are added to valid
# states, and if the result is also a valid state, then an edge exists
# in the graph
def build_elevator_paths(n):
    valid_paths = set()
    item_moves = [[(0, 1)],
                  [(1, 0)],
                  [(1, 1)],
                  [(0, 1), (0, 1)],
                  [(0, 1), (1, 0)],
                  [(1, 0), (0, 1)],
                  [(1, 0), (1, 0)]]
    for row in item_moves:
        row.extend([(0, 0)] * (n - len(row)))
        for permutation in permutations(row):
            valid_paths.add(permutation)
    return valid_paths

if __name__ == "__main__":
    main()