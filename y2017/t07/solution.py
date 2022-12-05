import re

from utils import read, p1, p2


def main():
    lines = read()

    tree = {}

    for x in lines:
        node, num, children = re.findall(r'(\w+) \((\d+)\)(?: -> (.*))?', x)[0]
        tree[node] = (int(num), children.split(', ') if children else [])

    root = (set(tree) - set(c for node in tree.values() for c in node[1])).pop()
    p1(root)

    weights_map = {}

    def get_weight(node):
        if node not in weights_map:
            w = tree[node][0]
            for c in tree[node][1]:
                w += get_weight(c)
            weights_map[node] = w
        return weights_map[node]

    x = root
    potential_answer = None
    while True:
        if tree[x][1]:
            weights = [get_weight(n) for n in tree[x][1]]
        else:
            break

        if all(w1 == w2 for w1, w2 in zip(weights, weights[1:])):
            break

        for i, (w1, w2, w3) in enumerate(zip(weights, weights[1:], weights[2:])):
            if w1 == w2 and w1 == w3:
                continue

            if w1 != w2 and w1 != w3:
                idx = i
                w = w2
            elif w2 != w1 and w2 != w3:
                idx = i + 1
                w = w3
            else:
                idx = i + 2
                w = w1
        x = tree[x][1][idx]
        potential_answer = tree[x][0] - get_weight(x) + w

    p2(potential_answer)
