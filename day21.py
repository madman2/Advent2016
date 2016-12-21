# Day 21: Scrambled Letters and Hash

from itertools import permutations

def main():

    with open('day21.txt') as f:
        lines = f.read().strip().split('\n')

    print("Part 1: {}".format(scramble("abcdefgh", lines)))

    for permutation in permutations("abcdefgh"):
        if scramble(permutation, lines) == "fbgdceah":
            print("Part 2: {}".format("".join(permutation)))
            break

def scramble(text, lines):
    text = list(text)

    for line in lines:
        words = line.split()

        if words[0] == 'swap' and words[1] == 'position':
            pos1 = int(words[2])
            pos2 = int(words[5])
            temp = text[pos1]
            text[pos1] = text[pos2]
            text[pos2] = temp
        elif words[0] == 'swap':
            letter1 = words[2]
            letter2 = words[5]
            letter1_idx = text.index(letter1)
            letter2_idx = text.index(letter2)
            text[letter1_idx] = letter2
            text[letter2_idx] = letter1
        elif words[0] == 'rotate' and words[1] == 'based':
            letter = words[6]
            index = text.index(letter)
            if index >= 4:
                index += 2
            else:
                index += 1
            index = index % len(text)
            text = text[-index:] + text[:-index]
        elif words[0] == 'rotate':
            n = int(words[2]) % len(text)
            if words[1] == 'right':
                n = -n
            text = text[n:] + text[:n]
        elif words[0] == 'reverse':
            pos1 = int(words[2])
            pos2 = int(words[4])
            text = text[:pos1] + list(reversed(text[pos1:pos2 + 1])) + text[pos2 + 1:]
        elif words[0] == 'move':
            pos1 = int(words[2])
            pos2 = int(words[5])
            temp = text.pop(pos1)
            text.insert(pos2, temp)
        else:
            print("Parsing error")

    return "".join(text)

if __name__ == "__main__":
    main()