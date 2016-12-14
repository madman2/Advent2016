# Day 03: Squares with Three Sides

def main():
    valid = 0
    total = 0

    with open('day03.txt') as f:
        for line in f:
            total += 1
            triangle = line.split()
            if validate(triangle):
                valid += 1
        print("Part 1: {}".format(valid))

    n = 0
    valid = 0
    triangles = [[0 for x in range(0, 3)] for y in range(0, 3)]

    with open('day03.txt') as f:
        for line in f:
            sides = line.split()
            triangles[n % 3] = sides
            if n % 3 == 2:
                for j in range(0, 3):
                    triangle = []
                    for i in range(0, 3):
                        triangle.append(triangles[i][j])
                    if validate(triangle):
                        valid += 1
            n += 1
        print("Part 2: {}".format(valid))

def validate(triangle):
    a = int(triangle[0])
    b = int(triangle[1])
    c = int(triangle[2])
    return a + b > c and b + c > a and a + c > b

if __name__ == "__main__":
    main()