# Day 10: Balance Bots

def main():
    bot_chips = dict()
    bot_instr = dict()
    output_chips = dict()
    output_instr = dict()

    with open('day10.txt') as f:
        for line in f:
            words = line.strip().split()
            if len(words) == 6:
                bot_number = int(words[5])
                chip_number = int(words[1])
                if bot_number in bot_chips:
                    val = bot_chips.pop(bot_number)
                    bot_chips[bot_number] = (val, chip_number)
                else:
                    bot_chips[bot_number] = chip_number
            else:
                bot_number = int(words[1])
                low_chip_number = int(words[6])
                high_chip_number = int(words[11])
                low_chip_recipient = words[5]
                high_chip_recipient = words[10]
                if low_chip_recipient == 'output' and high_chip_recipient == 'output':
                    output_instr[bot_number] = (low_chip_number, high_chip_number)
                    bot_instr[bot_number] = (-1, -1)
                elif words[5] == 'bot' and words[10] == 'bot':
                    bot_instr[bot_number] = (low_chip_number, high_chip_number)
                elif words[5] == 'output':
                    output_instr[bot_number] = (low_chip_number, -1)
                    bot_instr[bot_number] = (-1, high_chip_number)
                else:
                    output_instr[bot_number] = (-1, high_chip_number)
                    bot_instr[bot_number] = (low_chip_number, -1)

    wanted_bot = -1
    full_bots = [0]
    while len(full_bots) > 0:
        full_bots = []
        for key, value in bot_chips.items():
            if type(value) is tuple:
                full_bots.append(key)

        for key in full_bots:
            value = bot_chips[key]
            low_chip_number = min(value)
            high_chip_number = max(value)
            low_chip_recipient = bot_instr[key][0]
            high_chip_recipient = bot_instr[key][1]
            if low_chip_recipient < 0:
                insert_into_tuple_dict(output_chips, output_instr[key][0], low_chip_number)
            else:
                insert_into_tuple_dict(bot_chips, low_chip_recipient, low_chip_number)
                if type(bot_chips[key]) is tuple:
                    if 61 in bot_chips[key] and 17 in bot_chips[key]:
                        wanted_bot = key
            if high_chip_recipient < 0:
                insert_into_tuple_dict(output_chips, output_instr[key][1], high_chip_number)
            else:
                insert_into_tuple_dict(bot_chips, high_chip_recipient, high_chip_number)
                if type(bot_chips[key]) is tuple:
                    if 61 in bot_chips[key] and 17 in bot_chips[key]:
                        wanted_bot = key

            del bot_chips[key]

    print("Part 1: {}".format(wanted_bot))
    print("Part 2: {}".format(output_chips[0] * output_chips[1] * output_chips[2]))

def insert_into_tuple_dict(d, key, value):
    if key in d:
        temp = d.pop(key)
        d[key] = (temp, value)
    else:
        d[key] = value

if __name__ == "__main__":
    main()
