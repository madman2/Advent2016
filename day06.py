# Day 06: Signals and Noise

from collections import Counter

def main():
    counts = [[] for x in range(0, 8)]

    with open('day06.txt') as f:
        for line in f:
            i = 0
            for c in line.strip():
                counts[i].append(c)
                i += 1

    phrase1 = []
    phrase2 = []
    for column in counts:
        phrase1.append(Counter(column).most_common()[0][0])
        phrase2.append(sorted(Counter(column).most_common(), key = lambda x: (x[1]))[0][0])

    print("Part 1: {}".format(phrase1))
    print("Part 2: {}".format(phrase2))

if __name__ == "__main__":
    main()