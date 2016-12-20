# Day 11: Radioisotope Thermoelectric Generators

from itertools import combinations_with_replacement
from itertools import combinations
import heapq

def main():
    # start = ((1, 1), (1, 2), (1, 2), (3, 3), (3, 3))
    # end = ((4, 4), (4, 4), (4, 4), (4, 4), (4, 4))
    start = ((2, 1), (3, 1))
    end = ((4, 4), (4, 4))
    solve(start, end, 2)

def solve(start, end, n):
    floors = [i for i in range(1, 5)]
    c_pairs = [(i, j) for i in floors for j in floors]
    c_states = list(combinations_with_replacement(c_pairs, n))

    valid_states = []
    for state in c_states:
        unpaired_micro_floors = set()
        gen_floors = set()
        for micro_floor, gen_floor in state:
            gen_floors.add(gen_floor)
            if micro_floor != gen_floor:
                unpaired_micro_floors.add(micro_floor)
        if gen_floors.isdisjoint(unpaired_micro_floors):
            valid_states.append(state)

    adj = {key: set() for key in valid_states}
    edges = dict()
    for state1, state2 in combinations(valid_states, 2):
        elevator_path = get_elevator_path(state1, state2)
        if elevator_path:
            adj[state1].add(state2)
            adj[state2].add(state1)
            edges[state1, state2] = elevator_path
            edges[state2, state1] = elevator_path[::-1]
    
    print(adj[(3,3),(3,1)])

    p, min_cost = dijkstra(adj, edges, start, end)
    print(min_cost)

def dijkstra(adj, edges, s, t):
    Q = []
    d = {s: 0}
    Qd = {}
    p = {}
    visited_set = set([s])
    elevator = 1
    heapq.heapify(Q)

    for v in adj[s]:
        if edges[s, v][0] == elevator:
            d[v] = 1
            item = [d[v], edges[s, v][1], s, v]
            heapq.heappush(Q, item)
            Qd[v] = item

    while Q:
        cost, elevator, parent, u = heapq.heappop(Q)
        if u not in visited_set:
            p[u] = parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj[u]:
                if elevator == edges[(u, v)][0]:
                    if d.get(v):
                        if d[v] > 1 + d[u]:
                            d[v] = 1 + d[u]
                            Qd[v][0] = d[v]
                            Qd[v][2] = u
                            heapq._siftdown(Q, 0, Q.index(Qd[v]))
                    else:
                        d[v] = 1 + d[u]
                        item = [d[v], edges[u, v][1], u, v]
                        heapq.heappush(Q, item)
                        Qd[v] = item

    return None


def get_elevator_path(state1, state2):
    elevator = (0, 0)
    item_count = 0
    for pair1, pair2 in zip(state1, state2):
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