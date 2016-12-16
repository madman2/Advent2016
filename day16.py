# Day 16: Dragon Checksum

def main():
    input = '10011111011011001'
    disk = [int(c) for c in input]

    print("Part 1: {}".format("".join([str(bit) for bit in fill_disk(disk, 272)])))
    print("Part 2: {}".format("".join([str(bit) for bit in fill_disk(disk, 35651584)])))

def fill_disk(disk, size):
    while len(disk) < size:
        inverse_disk = [int(not x) for x in disk]
        disk.append(0)
        disk.extend(reversed(inverse_disk))

    checksum = disk[:size]
    while len(checksum) % 2 == 0:
        temp_checksum = []
        for i in range (0, len(checksum), 2):
            if (checksum[i] == checksum[i + 1]):
                temp_checksum.append(1)
            else:
                temp_checksum.append(0)
        checksum = temp_checksum

    return checksum

if __name__ == "__main__":
    main()