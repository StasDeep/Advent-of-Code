from collections import defaultdict

from utils import read, p1, p2


def main():
    lines = read()[1:]

    lines = [x.split('\n') for x in ('\n' + '\n'.join(lines)).split('\n$ ')[1:]]

    dirs = defaultdict(list)

    dir_stack = ['/']
    for cmd, *output in lines:
        cur_dir = '/'.join(dir_stack)
        if cmd == 'ls':
            for o in output:
                if o.startswith('dir'):
                    dirs[cur_dir].append(o[4:])
                else:
                    size, name = o.split()
                    dirs[cur_dir].append((int(size), name))

        if cmd[:2] == 'cd':
            d = cmd[3:]
            if d == '..':
                dir_stack.pop()
            else:
                dir_stack.append(d)

    weights = {}

    def get_weight(d):
        if d not in weights:
            weights[d] = 0
            for i in dirs[d]:
                if isinstance(i, str):
                    weights[d] += get_weight(f'{d}/{i}')
                else:
                    weights[d] += i[0]

        return weights[d]

    get_weight('/')
    p1(sum(w for w in weights.values() if w <= 100000))

    available = 70000000
    unused = 30000000

    to_delete = unused - (available - get_weight('/'))
    p2(sorted([(d, w) for d, w in weights.items() if w >= to_delete], key=lambda x: x[1])[0][1])
