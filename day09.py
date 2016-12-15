# Day 09: Explosives in Cyberspace

import re

pattern = r'\((\d+)x(\d+)\)'
capture = re.compile(pattern)

def main():
    f = open('day09.txt')
    data = f.read().strip()

    print("Part 1: {}".format(len(decompress(data))))
    print("Part 2: {}".format(sum(decompress_recurse(data))))

def decompress(data):
    i = 0
    result = ''
    while i < len(data):
        marker_begin = data.find('(', i)
        marker_end = data.find(')', i)

        if marker_begin == -1 or marker_end == -1:
            result += data[i:]
            break

        w, n = data[marker_begin + 1:marker_end].split('x')
        result += data[i:marker_begin]
        for j in range(0, int(n)):
            result += data[marker_end + 1:marker_end + int(w) + 1]
        i = marker_end + int(w) + 1

    return result

def decompress_recurse(data):
    while len(data) > 0:
        marker = re.search(capture, data)
        if marker is None:
            yield len(data)
            break

        yield len(data[:marker.start()])
        data = data[marker.end():]
        w, n = map(int, marker.groups())
        w_data = data[:w]
        data = data[w:]

        for count in decompress_recurse(w_data):
            yield n * count

if __name__ == "__main__":
    main()
