# Day 20: Firewall Rules

def main():
    blacklists = []

    with open('day20.txt') as f:
        for line in f:
            a, b = map(int, line.strip().split('-'))
            if len(blacklists) == 0:
                blacklists.append((a, b))
                continue

            found_range = False
            for idx, (start, end) in enumerate(list(blacklists)):
                if a < start and b > end:
                    blacklists.remove((start, end))
                if a >= start and a <= end:
                    found_range = True
                    if b > end:
                        blacklists.remove((start, end))
                        blacklists.append((start, b))
                elif b >= start and b <= end:
                    found_range = True
                    if a < start:
                        blacklists.remove((start, end))
                        blacklists.append((a, end))
            if not found_range:
                blacklists.append((a, b))

    blacklists = sorted(blacklists)

    part1_found = False
    allowed_ips = 0
    for range1, range2 in zip(blacklists, blacklists[1:]):
        if range2[0] - range1[1] > 1:
            if not part1_found:
                print("Part 1: {}".format(range1[1] + 1))
                part1_found = True
            allowed_ips += (range2[0] - range1[1] - 1)
    allowed_ips += (4294967295 - blacklists[len(blacklists) - 1][1])

    print("Part 2: {}".format(allowed_ips))

if __name__ == "__main__":
    main()