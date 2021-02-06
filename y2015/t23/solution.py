from utils import p1, p2, read


def main():
    lines = read()

    p1(simulate(lines, {"a": 0, "b": 0})["b"])
    p2(simulate(lines, {"a": 1, "b": 0})["b"])


def simulate(lines, env):
    cur_idx = 0
    while cur_idx < len(lines):
        instruction = lines[cur_idx]
        cmd, arg, *rest = instruction.split()
        arg = arg.strip(",")
        if cmd == "hlf":
            env[arg] = env[arg] // 2
        elif cmd == "inc":
            env[arg] += 1
        elif cmd == "tpl":
            env[arg] *= 3
        elif cmd == "jmp":
            cur_idx += int(arg)
            continue
        elif cmd == "jie":
            if env[arg] % 2 == 0:
                cur_idx += int(rest[0])
                continue
        elif cmd == "jio":
            if env[arg] == 1:
                cur_idx += int(rest[0])
                continue
        cur_idx += 1

    return env
