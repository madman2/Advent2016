# Day 05: How About a Nice Game of Chess?

import hashlib

def main():

    puzzle_input = 'uqwqemis'
    idx = 0
    pwd1_n = 0
    pwd2_n = 0
    password1 = []
    password2 = ['g' for x in range(0, 8)]
    while pwd2_n < 8:
        hash_result = 'ffffffffffffffffffffffffffffffff'
        while int(hash_result[:5], 16) != 0:
            m = hashlib.md5()
            m.update(puzzle_input.encode('utf-8'))
            m.update(str(idx).encode('utf-8'))
            hash_result = m.hexdigest()
            idx += 1

        chr_digit = hash_result[5]
        int_digit = int(hash_result[5], 16)

        if pwd1_n < 8:
            password1.append(chr_digit)
            pwd1_n += 1

        if int_digit < 8:
            if password2[int_digit] == 'g':
                password2[int_digit] = hash_result[6]
                pwd2_n += 1

    print("Part 1: {}".format(password1))
    print("Part 2: {}".format(password2))

if __name__ == "__main__":
    main()