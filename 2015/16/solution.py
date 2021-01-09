import re

from utils import read, p1, p2


inp = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

lt_fields = ["pomeranians", "goldfish"]
gt_fields = ["cats", "trees"]


def main():
    lines = read()

    exp = dict(pair.split(": ") for pair in inp.split("\n"))
    for k in exp:
        exp[k] = int(exp[k])

    m = {}
    "Sue 1: cars: 9, akitas: 3, goldfish: 0"
    for line in lines:
        sue, params = line.split(": ", 1)
        m[sue] = dict(
            pair.split(": ")
            for pair in params.split(", ")
        )

    for v in m.values():
        for k in v:
            v[k] = int(v[k])

    for sue, params in m.items():
        if all(exp[field] == params[field] for field in params):
            p1(sue.split()[-1])

        if (
            all(exp[field] == params[field] for field in params if field not in lt_fields + gt_fields)
            and all(exp[field] > params[field] for field in lt_fields if field in params)
            and all(exp[field] < params[field] for field in gt_fields if field in params)
        ):
            p2(sue.split()[-1])
