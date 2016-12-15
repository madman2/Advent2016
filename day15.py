# Day 15: Timing is Everything

def main():
    with open('day15.txt') as f:
        positions = []
        states = []
        for line in f:
            words = line.split()
            positions.append((int(words[3])))
            states.append(int(words[11][:len(words[11]) - 1]))

    i = 0
    part1 = False
    while True:
        i += 1
        for idx, state in enumerate(states):
            states[idx] = (state + 1) % positions[idx]

        if states[0] == (positions[0] - 1) % positions[0] and \
            states[1] == (positions[1] - 2) % positions[1] and \
            states[2] == (positions[2] - 3) % positions[2] and \
            states[3] == (positions[3] - 4) % positions[3] and \
            states[4] == (positions[4] - 5) % positions[4] and \
            states[5] == (positions[5] - 6) % positions[5]:
            if not part1:
                print("Part 1: {}".format(i))
                part1 = True
            if states[6] == (positions[6] - 7) % positions[6]:
                print("Part 2: {}".format(i))
                break

if __name__ == "__main__":
    main()
