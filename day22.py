# Day 22: Grid Computing

from itertools import permutations
import re

def main():
    with open('day22.txt') as f:
        lines = f.read().strip().split('\n')

    lines = lines[2:]
    grid = build_grid(lines)

    viable_nodes = 0
    for node1, node2 in permutations(grid, 2):
        if node2[1] >= node1[0] and node1[0] != 0:
            viable_nodes += 1

    print("Part 1: {}".format(viable_nodes))

def build_grid(lines):
    get_numbers = re.compile('(\d+)T')
    grid = [0 for i in range(0, len(lines))]
    for idx, line in enumerate(lines):
        grid[idx] = tuple(map(int, re.findall(get_numbers, line)[1:]))

    return grid

def solve():
    pass


if __name__ == "__main__":
    main()