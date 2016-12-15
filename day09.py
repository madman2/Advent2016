# Day 09: Explosives in Cyberspace

def main():
    f = open('day09.txt')
    data = f.read().strip()

    print("Part 1: {}".format(len(decompress(data))))
    print("Part 2: {}".format(len(decompress_recurse(data))))

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
    new_data = decompress(data)
    old_data = []

    while len(new_data) > len(old_data):
        old_data = new_data
        new_data = decompress(old_data)
        print(len(new_data))

    return new_data

if __name__ == "__main__":
    main()
