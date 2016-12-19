# Day 13: A Maze of Twisty Little Cubicles

import heapq

class MazeSolver:
    def __init__(self, key, wall_func):
        self.start = None
        self.end = None
        self.key = key
        self.wall_func = wall_func
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = dict()

    def initialize(self):
        self.start = None
        self.end = None
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = dict()

    def solve(self, start, end):
        self.start = start
        self.end = end
        start_cell = self.get_cell(self.start)
        end_cell = self.get_cell(self.end)
        heapq.heappush(self.opened, (start_cell.f, self.start))
        while(len(self.opened)):
            f, coord = heapq.heappop(self.opened)
            cell = self.get_cell(coord)
            self.closed.add(coord)
            if coord == self.end:
                return (int(cell.f / 10))

            adj_cells = self.get_adjacent(coord)
            for adj_cell in adj_cells:
                if not adj_cell.wall and adj_cell.coord not in self.closed:
                    if (adj_cell.f, adj_cell.coord) in self.opened:
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell.coord))
        return -1

    def heuristic(self, coord):
        return 10 * (abs(self.end[0] - coord[0]) + abs(self.end[1] - coord[1]))

    def update_cell(self, adj, cell):
        adj.g = cell.g + 10
        adj.h = self.heuristic(adj.coord)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def get_adjacent(self, coord):
        x = coord[0]
        y = coord[1]
        adj = []
        adj.append(self.get_cell((x + 1, y)))
        adj.append(self.get_cell((x, y + 1)))
        if x > 0:
            adj.append(self.get_cell((x - 1, y)))
        if y > 0:
            adj.append(self.get_cell((x, y - 1)))

        return adj

    def get_cell(self, coord):
        if coord in self.cells:
            return self.cells[coord]
        else:
            self.cells[coord] = Cell(coord, self.wall_func(coord, self.key))
            return self.cells[coord]

class Cell:
    def __init__(self, coord, wall):
        self.wall = wall
        self.coord = coord
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0

def main():
    key = 1362
    start = (1, 1)
    end = (31, 39)

    solver = MazeSolver(key, coord_is_wall)
    print("Part 1: {}".format(solver.solve(start, end)))

    unique = 0
    for x in range(0, 52):
        for y in range(0, 52):
            path_length = solver.solve((1, 1), (x, y))
            if path_length >= 0 and path_length <= 50:
                unique += 1
            solver.initialize()

    print("Part 2: {}".format(unique))

def coord_is_wall(coord, input):
    x = coord[0]
    y = coord[1]
    return bin(x*x + 3*x + 2*x*y + y + y*y + input).count('1') % 2

if __name__ == "__main__":
    main()
