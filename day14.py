# Day 14: One-Time Pad

import itertools
import hashlib
import re

def main():

    salt = 'jlmsuwbz'
    three_regex = re.compile(r'(.)\1{2}')
    five_regex = re.compile(r'(.)\1{4}')

    three_matches = [[] for i in range(0, 16)]

    digits_found = 0
    max_key = 0
    key_list = []

    for i in itertools.count():
        m = hashlib.md5()
        m.update(salt.encode('utf_8'))
        m.update(str(i).encode('utf_8'))
        result = m.hexdigest()

        # Comment these lines out for Part 1
        for _ in range(0, 2016):
            result = hashlib.md5(result.encode('utf_8')).hexdigest()

        five_match = re.search(five_regex, result)
        if five_match:
            keys = [x for x in three_matches[int(five_match.group(1), 16)] if i - x <= 1000]
            for key in keys:
                if key > max_key:
                    max_key = key
                key_list.append(key)
                three_matches[int(five_match.group(1), 16)].remove(key)
            digits_found += len(keys)
            if digits_found > 64 and i - 1000 > sorted(key_list)[63]:
                print("Part 2: {}".format(sorted(key_list)[63]))
                break

        three_match = re.search(three_regex, result)
        if three_match:
            three_matches[int(three_match.group(1), 16)].append(i)

if __name__ == "__main__":
    main()
