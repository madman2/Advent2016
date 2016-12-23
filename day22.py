# Day 22: Grid Computing

from itertools import permutations
import re
import math

class StorageGrid:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[(0, 0) for i in range(0, self.dim)] for j in range(0, self.dim)]

    def build_grid(self, lines):
        get_numbers = re.compile(r'(\d+)T')
        for idx, line in enumerate(lines):
            self.grid[idx % self.dim][math.floor(idx / self.dim)] = tuple(map(int, re.findall(get_numbers, line)))

    def count_viable_nodes(self):
        viable_nodes = 0
        for node1, node2 in permutations(self.grid, 2):
            if node2[2] >= node1[1] and node1[1] != 0:
                viable_nodes += 1

        return viable_nodes

    def get_adj_nodes(self, x, y):
        if x > 0:
            yield (x - 1, y), self.grid[y][x - 1]
        if y > 0:
            yield (x, y - 1), self.grid[y - 1][x]
        if x < self.dim - 1:
            yield (x + 1, y), self.grid[y][x + 1]
        if y < self.dim - 1:
            yield (x, y + 1), self.grid[y + 1][x]

    def get_available_moves(self):
        avail_moves = []
        for y, row in enumerate(self.grid):
            for x, node in enumerate(row):
                for adj_node_coord, adj_node in self.get_adj_nodes(x, y):
                    if adj_node[2] > node[1] and node[1] > 0:
                        avail_moves.append(((x, y), adj_node_coord))

        print(avail_moves)

    def print_grid(self):
        for row in self.grid:
            print('|', end='')
            for node in row:
                for _ in range(0, 3 if node[1] < 10 else 2 if node[1] < 100 else 1):
                    print(' ', end='')
                print('/'.join(map(str, node[:2][::-1])), end='')
                for _ in range(0, 2 if node[0] < 100 else 1):
                    print(' ', end='')
                print('|', end='')
            print()

def main():
    with open('day22.txt') as f:
        lines = f.read().strip().split('\n')

    lines = lines[2:]
    storage_grid = StorageGrid(int(math.sqrt(len(lines))))
    storage_grid.build_grid(lines)
    print("Part 1: {}".format(storage_grid.count_viable_nodes()))
    # storage_grid.print_grid()

    # To solve part 2, I just printed out the grid and solved it by hand
    print("Part 2: 207")

if __name__ == "__main__":
    main()