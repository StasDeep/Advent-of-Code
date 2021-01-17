from utils import read, p1, p2


def nth_repl(s, sub, repl, n):
    find = -1
    for i in range(n + 1):
        find = s.find(sub, find + 1)
        if find == -1:
            break
        if i == n:
            return s[:find] + repl + s[find + len(sub):]
    return s


def get_all_possible_replacements(line, replacements):
    molecules = set()
    for sub, repl in sorted(replacements, key=lambda x: x[0]):
        for i in range(line.count(sub)):
            new_molecule = nth_repl(line, sub, repl, i)
            if new_molecule != line and new_molecule not in molecules:
                yield new_molecule
                molecules.add(new_molecule)


def main():
    replacements, line = "\n".join(read()).split("\n\n")
    replacements = [((s := repl.split())[0], s[2]) for repl in replacements.split("\n")]

    p1(len(list(get_all_possible_replacements(line, replacements))))

    inv_replacements = [(y, x) for x, y in replacements]

    m = {line: 0}
    stack = [line]
    while "e" not in stack and stack:
        molecule = stack.pop()
        for smaller_molecule in get_all_possible_replacements(molecule, inv_replacements):
            if "e" in smaller_molecule and smaller_molecule != "e":
                continue

            if smaller_molecule not in m:
                stack.append(smaller_molecule)

            m.setdefault(smaller_molecule, m[molecule] + 1)

    p2(m["e"])
