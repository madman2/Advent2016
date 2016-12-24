# Day 24: Air Duct Spelunking

import heapq
from itertools import combinations
from itertools import permutations

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = None
        self.start = None
        self.width = len(maze[0])
        self.height = len(maze)
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = dict()

    def initialize(self, start, end):
        self.start = start
        self.end = end
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = dict()
        for row in self.maze:
            for cell in row:
                cell.reset()

    def solve(self, start, end):
        self.initialize(start, end)
        start_cell = self.get_cell(self.start)
        end_cell = self.get_cell(self.end)
        heapq.heappush(self.opened, (start_cell.f, self.start))
        while(len(self.opened)):
            f, coord = heapq.heappop(self.opened)
            cell = self.get_cell(coord)
            self.closed.add(coord)
            if coord == self.end:
                return (int(cell.f / 10))

            for adj_cell in self.get_adjacent_cells(coord):
                if not adj_cell.wall and adj_cell.coord not in self.closed:
                    if (adj_cell.f, adj_cell.coord) in self.opened:
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell.coord))
        return -1

    def heuristic(self, cell):
        return 10 * (abs(self.end[0] - cell[0]) + abs(self.end[1] - cell[1]))

    def get_cell(self, coord):
        return self.maze[coord[1]][coord[0]]

    def update_cell(self, adj, cell):
        adj.g = cell.g + 10
        adj.h = self.heuristic(adj.coord)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def get_adjacent_cells(self, coord):
        x = coord[0]
        y = coord[1]
        if x < self.width - 1:
            yield self.maze[y][x + 1]
        if y < self.height - 1:
            yield self.maze[y + 1][x]
        if x > 0:
            yield self.maze[y][x - 1]
        if y > 0:
            yield self.maze[y - 1][x]

class Cell:
    def __init__(self, coord, val):
        self.wall = (val == '#')
        self.val = val
        self.coord = coord
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0

    def reset(self):
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0

def build_maze(lines):
    maze = []
    for row_index, cells in enumerate(lines):
        maze.append([Cell((col_index, row_index), cell) for col_index, cell in enumerate(cells)])
    return maze

def get_poi_coords(maze):
    poi_list = []
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            try:
                i = int(cell.val)
                poi_list.append((i, (col_index, row_index)))
            except ValueError:
                pass
    return sorted(poi_list)

def find_shortest_paths(solver, poi_coords):
    shortest_paths = dict()
    for pair in combinations(poi_coords, 2):
        dist = solver.solve(pair[0][1], pair[1][1])
        shortest_paths[pair[0][0], pair[1][0]] = dist
        shortest_paths[pair[1][0], pair[0][0]] = dist
    return shortest_paths

def main():
    with open('day24.txt') as f:
        maze = build_maze(f.read().split('\n'))
    poi_coords = get_poi_coords(maze)
    solver = MazeSolver(maze)
    shortest_paths = find_shortest_paths(solver, poi_coords)

    path_lengths = []
    for sequence in permutations(poi_coords[1:]):
        new_sequence = [poi_coords[0]]
        new_sequence.extend(sequence)
        sum = 0
        for start, end in zip(new_sequence, new_sequence[1:]):
            sum += shortest_paths[start[0], end[0]]
        path_lengths.append(sum)

    print("Part 1: %s" % min(path_lengths))

    path_lengths = []
    for sequence in permutations(poi_coords[1:]):
        new_sequence = [poi_coords[0]]
        new_sequence.extend(sequence)
        new_sequence.append(poi_coords[0])
        sum = 0
        for start, end in zip(new_sequence, new_sequence[1:]):
            sum += shortest_paths[start[0], end[0]]
        path_lengths.append(sum)

    print("Part 2: %s" % min(path_lengths))

if __name__ == "__main__":
    main()
