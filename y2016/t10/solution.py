import math
import re
from collections import defaultdict
from typing import List

from utils import read, p1, p2


def main():
    commands = read()
    bc = BotController()
    bc.run(commands)
    p2(math.prod(math.prod(bc.outputs[i].chips) for i in range(3)))


class InstructionGive:

    def __init__(self, low_to, high_to):
        self.low_to = low_to
        self.high_to = high_to

    def execute(self, low_chip, high_chip):
        self.low_to.chips.append(low_chip)
        self.high_to.chips.append(high_chip)


class BotController:

    def __init__(self):
        self.bots = defaultdict(Bot)
        self.outputs = defaultdict(Output)

    def evaluate(self, command):
        init_match = re.match(r"value (\d+) goes to bot (\d+)", command)
        give_match = re.match(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", command)

        if init_match:
            chip_val, bot_num = init_match.groups()
            self.bots[int(bot_num)].chips.append(int(chip_val))
        elif give_match:
            donor_num, low_type, low_num, high_type, high_num = give_match.groups()

            give_instruction = InstructionGive(
                low_to=self.bots[int(low_num)] if low_type == "bot" else self.outputs[int(low_num)],
                high_to=self.bots[int(high_num)] if high_type == "bot" else self.outputs[int(high_num)],
            )

            self.bots[int(donor_num)].instructions.append(give_instruction)
        else:
            raise ValueError("Unknown format of command")

    def check_bots(self):
        while True:
            bots_are_passive = True

            for bot_num, bot in self.bots.items():
                if bot.ready_to_proceed():
                    if 17 in bot.chips and 61 in bot.chips:
                        p1(bot_num)

                    bot.run()
                    bots_are_passive = False
                    break

            if bots_are_passive:
                break

    def run(self, commands: List[str]):
        for command in commands:
            self.evaluate(command)
            self.check_bots()


class Output:

    def __init__(self):
        self.chips: List[int] = []

    def __repr__(self):
        return f"<Output Bin. Chips: {', '.join(str(chip) for chip in self.chips)}>"


class Bot:

    def __init__(self):
        self.chips: List[int] = []
        self.instructions: List[InstructionGive] = []

    def ready_to_proceed(self):
        return len(self.chips) == 2 and self.instructions

    def run(self):
        instruction = self.instructions.pop(0)
        instruction.execute(*sorted(self.chips))
        self.chips = []
