# Day 18: Like a Rogue

def main():
    with open('day18.txt') as f:
        first_row = f.read().strip()

    print("Part 1: {}".format(count_safe_space(first_row, 40)))
    print("Part 2: {}".format(count_safe_space(first_row, 400000)))

def count_safe_space(first_row, n):
    tiles = [['.' for i in range(0, len(first_row) + 2)] for j in range(0, n)]
    tiles[0][1:len(first_row) + 1] = list(first_row)

    total_traps = 0
    for c in first_row:
        if c == '^':
            total_traps += 1

    count = 0
    for row1, row2 in zip(tiles, tiles[1:n]):
        for idx, _ in enumerate(row2):
            if idx == 0 or idx == len(row2) - 1:
                continue
            count += 1
            prev_tiles = row1[idx-1:idx+2]
            if prev_tiles[0] == '^' and prev_tiles[1] == '^' and prev_tiles[2] == '.':
                row2[idx] = '^'
                total_traps += 1
            elif prev_tiles[0] == '.' and prev_tiles[1] == '^' and prev_tiles[2] == '^':
                row2[idx] = '^'
                total_traps += 1
            elif prev_tiles[0] == '^' and prev_tiles[1] == '.' and prev_tiles[2] == '.':
                row2[idx] = '^'
                total_traps += 1
            elif prev_tiles[0] == '.' and prev_tiles[1] == '.' and prev_tiles[2] == '^':
                row2[idx] = '^'
                total_traps += 1

    total_tiles = n * len(first_row)
    return total_tiles - total_traps

if __name__ == "__main__":
    main()