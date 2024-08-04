import os
import sys
import re
import math

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'inputs')
RE_VALUE = r'value (\d+) goes to bot (\d+)'
RE_BOT_GIVE = r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'


def prepare_input_file(filename=os.path.basename(__file__).replace('.py',
                       '.txt')):
    file_path = os.path.join(INPUT_DIR, filename)
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    return lines


class Bot:
    def __init__(self, i, chips=[]) -> None:
        self.id = i
        self.chips = set(chips.copy())

    def __repr__(self) -> str:
        return f"Bot {self.id} has the following chips: {self.chips}"

    def get_low_chip(self) -> int:
        if len(self.chips) != 2:
            return -1
        return sorted(list(self.chips))[0]

    def get_high_chip(self) -> int:
        if len(self.chips) != 2:
            return -1
        return sorted(list(self.chips))[1]

    def add_chip(self, chip: int) -> None:
        if chip != -1:
            self.chips.add(chip)
        if len(self.chips) > 2:
            print(f"Bot {self.id} has already too many chips ({self.chips})" \
                   "({chip})")


def main():
    if len(sys.argv) == 2:
        lines = prepare_input_file(sys.argv[1])
    else:
        lines = prepare_input_file()
    print(f"Received {len(lines)} instructions")

    bots = {}
    outputs = {}
    # create bot and outputs arrays:
    for line in lines:
        if re.match(RE_VALUE, line):
            value, bot = re.search(RE_VALUE, line).groups()
            if bot not in bots.keys():
                bots[bot] = Bot(bot)
        elif re.match(RE_BOT_GIVE, line):
            giver, l_type, l_nr, h_type, h_nr = \
                    re.search(RE_BOT_GIVE, line).groups()
            for bot in [(giver, 'bot'), (l_nr, l_type), (h_nr, h_type)]:
                if bot[1] == 'bot':
                    bots[bot[0]] = Bot(bot[0])
                elif bot[1] == 'output':
                    outputs[bot[0]] = set()
                else:
                    print(f"Received unkown Type { bot[1]}")

    # part 1
    part1 = part2 = False
    while True:
        for line in lines:
            if re.match(RE_VALUE, line):
                value, bot_name = re.search(RE_VALUE, line).groups()
                bots[bot_name].add_chip(int(value))
            elif re.match(RE_BOT_GIVE, line):
                giver, l_type, l_nr, h_type, h_nr = re.search(RE_BOT_GIVE, line).groups()
                if l_type == 'bot':
                    if bots[giver].get_low_chip() != -1:
                        bots[l_nr].add_chip(bots[giver].get_low_chip())
                elif l_type == 'output':
                    if bots[giver].get_low_chip() != -1:
                        outputs[l_nr].add(bots[giver].get_low_chip())
                if h_type == 'bot':
                    if bots[giver].get_high_chip() != -1:
                        bots[h_nr].add_chip(bots[giver].get_high_chip())
                elif h_type == 'output':
                    if bots[giver].get_high_chip() != -1:
                        outputs[h_nr].add(bots[giver].get_high_chip())

                # part 1
                check_value = set([61, 17])
                if not part1 and any(bot.chips == check_value for bot in bots.values()):
                    for bot in bots.values():
                        if bot.chips == check_value:
                            print(f"Part 1: {bot.id}")
                            part1 = True

                # part 2
                part2_elements = ['0', '1', '2']
                if not part2 and \
                        all(len(outputs[el]) > 0 for el in part2_elements):
                    part2 = math.prod([list(outputs[el])[0] for el in
                                       part2_elements])
                    print(f"Part 2: {part2}")
                    part2 = True

                # check is both parts have been solved
                if part1 and part2:
                    exit(1)


if __name__ == '__main__':
    main()
