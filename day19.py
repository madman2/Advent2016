# Day 19: An Elephant Named Joseph

from math import floor

def main():
    my_input = 3004953
    print("Part 1: {}".format(white_elephant_A(my_input)))
    print("Part 2: {}".format(white_elephant_B(my_input)))

def white_elephant_A(n):
    mod = 1
    while mod <= n:
        mod *= 2
    mod /= 2
    return int(1 + 2 * (n % mod))

def white_elephant_B(n):
    mod = 1
    while mod <= n:
        mod *= 3
    mod /= 3
    if n == mod:
        return n
    elif n < 2 * mod:
        return int(n % mod)
    else:
        return int(mod + 2 * (n % mod))

if __name__ == "__main__":
    main()