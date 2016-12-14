# Day 02: Bathroom Security

def main():
    with open('day02.txt') as codes:
        lines = codes.readlines()

    numpad = [[x + 3*y for x in range(1, 4)] for y in range(0, 3)]
    numpad2 = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 10, 11, 12, 0], [0, 0, 13, 0, 0]]

    x_idx = 1
    y_idx = 1
    i = 1

    print('Part 1\n')

    for code in lines:
        for c in code:
            if c == 'U' and y_idx > 0:
                y_idx -= 1
            elif c == 'R' and x_idx < 2:
                x_idx += 1
            elif c == 'D' and y_idx < 2:
                y_idx += 1
            elif c == 'L' and x_idx > 0:
                x_idx -= 1
        print('Digit #{}: {}'.format(i, numpad[y_idx][x_idx]))
        i += 1

    print('\nPart 2\n')

    x_idx = 0
    y_idx = 2
    i = 0

    for code in lines:
        for c in code:
            if c == 'U' and y_idx > 0:
                if numpad2[x_idx][y_idx - 1] != 0:
                    y_idx -= 1
            elif c == 'R' and x_idx < 4:
                if numpad2[x_idx + 1][y_idx] != 0:
                    x_idx += 1
            elif c == 'D' and y_idx < 4:
                if numpad2[x_idx][y_idx + 1] != 0:
                    y_idx += 1
            elif c == 'L' and x_idx > 0:
                if numpad2[x_idx - 1][y_idx] != 0:
                    x_idx -= 1
        print('Digit #{}: {}'.format(i, numpad2[y_idx][x_idx]))
        i += 1


if __name__ == "__main__":
    main()