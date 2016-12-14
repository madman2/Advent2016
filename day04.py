# Day 04: Security through Obscurity

from collections import Counter

def main():
    total = 0
    with open('day04.txt') as f:
        for line in f:
            total += process(line)

    print("Part 1: {}".format(total))

def process(line):
    checksum = line[line.find('[') + 1:line.find(']')]
    name, id_str = line[0:line.find('[')].rsplit('-', 1)
    no_dash_name = name.replace('-','')

    counts = Counter(no_dash_name).most_common()
    common = sorted(counts, key = lambda x: (-x[1], x[0]))

    for i in range(0, 5):
        if common[i][0] not in checksum:
            return 0
    
    id = int(id_str)
    result = ''

    for c in name:
        if c == '-':
            result += ' '
        else:
            rotation = (ord(c) + (id % 26))
            if rotation > ord('z'):
                rotation = ((rotation % ord('z')) + ord('a')) - 1
            result += chr(rotation)

    if 'northpole' in result:
        print("Part 2: {}".format(id))

    return id

if __name__ == "__main__":
    main()