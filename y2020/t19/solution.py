import re
from functools import lru_cache

from utils import read, p1, p2


def main():
    rules, lines = "\n".join(read()).split("\n\n")
    lines = lines.split("\n")
    rules = {
        int(rule.split(":")[0]): [
            [int(z) if z.isdigit() else z[1:-1] for z in x.split()]
            for x in rule.split(": ")[1].split(" | ")
        ]
        for rule in rules.split("\n")
    }

    pattern = get_pattern_from_rules(rules, part=1)
    p1(sum(bool(re.fullmatch(pattern, line)) for line in lines))
    pattern = get_pattern_from_rules(rules, part=2)
    p2(sum(bool(re.fullmatch(pattern, line)) for line in lines))


def get_pattern_from_rules(rules, part):
    @lru_cache
    def get_pattern(idx):
        rule = rules[idx]
        if isinstance(rule[0][0], str):
            return re.escape(rule[0][0])

        if part == 2:
            if idx == 8:
                return f"({get_pattern(42)})+"

            if idx == 11:
                patterns = []
                for i in range(1, 5):
                    patterns.append(f"({get_pattern(42)}){{{i}}}({get_pattern(31)}){{{i}}}")
                return f"({'|'.join(patterns)})"

        or_rules = ["".join(get_pattern(x) for x in or_rule) for or_rule in rule]
        return f"({'|'.join(or_rules)})"

    return get_pattern(0)
