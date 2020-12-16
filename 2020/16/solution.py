import math
from collections import defaultdict

from utils import read, p1, p2


def main():
    rules, my_ticket, other_tickets = [
        x.split("\n") for x in "\n".join(read()).split("\n\n")
    ]
    my_ticket = list(map(int, my_ticket[1].split(",")))
    other_tickets = [list(map(int, x.split(","))) for x in other_tickets[1:]]
    rules = {
        rule.split(":")[0]: [
            [int(x) for x in rule.split(" ")[i].split("-")] for i in [-3, -1]
        ]
        for rule in rules
    }

    c = 0
    for t in other_tickets:
        for n in t:
            if all(
                not (rule[0][0] <= n <= rule[0][1] or rule[1][0] <= n <= rule[1][1])
                for rule in rules.values()
            ):
                c += n

    p1(c)

    valid_tickets = [
        t
        for t in other_tickets
        if not any(
            all(
                not (rule[0][0] <= n <= rule[0][1] or rule[1][0] <= n <= rule[1][1])
                for rule in rules.values()
            )
            for n in t
        )
    ]

    d = defaultdict(list)
    for rule_name, rule in rules.items():
        for ti in range(len(my_ticket)):
            if all(
                rule[0][0] <= n <= rule[0][1] or rule[1][0] <= n <= rule[1][1]
                for n in [t[ti] for t in valid_tickets]
            ):
                d[rule_name].append(ti)

    s = sorted(d.items(), key=lambda x: len(x[1]))
    ridxs = [None] * len(my_ticket)
    while None in ridxs:
        for name, idxs in s:
            if name not in ridxs:
                for idx in idxs:
                    if ridxs[idx] is None:
                        ridxs[idx] = name

    dep_idx = [i for i, r in enumerate(ridxs) if r.startswith("departure")]
    p2(math.prod([my_ticket[i] for i in dep_idx]))
