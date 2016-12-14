# Day 08: Two-Factor Authentication

def main():
    pixels = [[0 for x in range(0, 50)] for y in range(0, 6)]

    with open('day08.txt') as f:
        for line in f:
            words = line.split()
            if words[0] == 'rect':
                rect(pixels, int(words[1].split('x')[0]), int(words[1].split('x')[1]))
                # print(pixels)
            elif words[0] == 'rotate':
                if words[1] == 'row':
                    rotate_row(pixels, int(words[2].split('=')[1]), int(words[4]))
                else:
                    rotate_col(pixels, int(words[2].split('=')[1]), int(words[4]))

    total = 0
    for row in pixels:
        print(row)
        total += sum(row)

    print("Part 1: {}".format(total))

def rect(grid, cols, rows):
    for j in range(0, rows):
        grid[j][0:cols] = [1 for i in range(0, cols)]

def rotate_row(grid, row, n):
    grid[row][:] = rotate(grid[row][:], n)

def rotate_col(grid, col, n):
    result = rotate([row[col] for row in grid], n)
    for idx, row in enumerate(grid):
        row[col] = result[idx]

def rotate(l, n):
    return l[-n:] + l[:-n]

if __name__ == "__main__":
    main()
