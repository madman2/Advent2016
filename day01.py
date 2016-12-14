# Day 01: No Time for a Taxicab

import csv

def main():
    blocks = [0, 0, 0, 0]
    orientation = 0
    stops = dict()
    revisit = False

    with open('day01.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row = [x.strip() for x in row]
            for val in row:
                turn = val[0]
                dist = int(val[1:])
                if turn == 'R':
                    orientation = (orientation + 1) % 4
                else:
                    orientation = (orientation - 1) % 4

                for i in range(0, dist):
                    blocks[orientation] += 1

                    x_loc = blocks[1] - blocks[3]
                    y_loc = blocks[0] - blocks[2]

                    if x_loc not in stops:
                        stops[x_loc] = [y_loc]
                    else:
                        if y_loc in stops[x_loc]:
                            if not revisit:
                                print("Part 2: {}".format(abs(x_loc) + abs(y_loc)))
                                revisit = True
                        stops[x_loc].append(y_loc)

    print("Part 1: {}".format(abs(blocks[0] - blocks[2]) + abs(blocks[1] - blocks[3])))

if __name__ == "__main__":
    main()
