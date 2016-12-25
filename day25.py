# Day 25: Clock Signal

from math import floor
from itertools import count

def main():
    for i in count(1):
        transmit = []
        emulate_assembunny(i, transmit)
        if sum(transmit[::2]) == 0 and sum(transmit[1::2]) == len(transmit[1::2]):
            print("Part 1: %s" % i)
            break

def emulate_assembunny(n, transmit):
    n = n + 2541
    while n > 0:
        transmit.append(n % 2)
        n = floor(n / 2)

if __name__ == "__main__":
    main()
