# Day 22: Grid Computing

from itertools import permutations

def main():
    with open('day22.txt') as f:
        lines = f.read().strip().split('\n')

    lines = lines[2:]
    nodes = []
    for line in lines:
        words = line.split()
        nodes.append((int(words[2][:len(words[2]) - 1]), int(words[3][:len(words[3]) - 1])))

    viable_nodes = 0
    for node1, node2 in permutations(nodes, 2):
        if node2[1] >= node1[0] and node1[0] != 0:
            viable_nodes += 1

    print(viable_nodes)


if __name__ == "__main__":
    main()