from utils import read, p1, p2
import operator as op

OP = {
    'NOT': op.invert,
    'AND': op.and_,
    'OR': op.or_,
    'LSHIFT': op.lshift,
    'RSHIFT': op.rshift,
}


def main():
    lines = read()

    a_val = run(lines, {}, 'a')
    p1(a_val)
    p2(run(lines, {'b': a_val}, 'a'))


def run(lines, env, wait_for):
    while wait_for not in env:
        for line in lines:
            expr, var = line.split(' -> ')

            if var in env:
                continue

            expr_split = expr.split()

            operation = next((x for x in expr_split if x.isupper()), None)
            operands = [int(x) if x.isdigit() else env.get(x) for x in expr_split if x != operation]
            if None in operands:
                continue

            if operation is None:
                env[var] = operands[0]
            elif operation in OP:
                env[var] = OP[operation](*operands) % 2 ** 16
    return env[wait_for]
