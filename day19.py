# Day 19: An Elephant Named Joseph

from math import floor

class Elf:
    def __init__(self, index):
        self.index = index
        self.presents = 0

def main():
    print(white_elephant(10))

def white_elephant(n):
    elves = [Elf(x + 1) for x in range(0, n)]

    current_elf = 0
    while len(elves) > 1:
        cross_elf = get_cross_elf(current_elf, len(elves))
        elves[current_elf].presents += elves[cross_elf].presents
        del elves[cross_elf]
        if current_elf == len(elves):
            current_elf = len(elves) - 1
        current_elf = (current_elf + 1) % len(elves)

    return elves[current_elf].index

def get_next_elf(current_elf, total_elves):
    return (current_elf + 1) % total_elves

def get_cross_elf(current_elf, total_elves):
    return (current_elf + floor(total_elves / 2)) % total_elves

if __name__ == "__main__":
    main()