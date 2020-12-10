from utils import read


def run(lines):
    lines_read = set()
    acc = 0
    line_to_read = 0
    infinite = False

    while True:
        if line_to_read in lines_read:
            infinite = True
            break

        if line_to_read >= len(lines):
            break

        line = lines[line_to_read]
        lines_read.add(line_to_read)
        cmd, arg = line.split()
        arg = int(arg.strip("+"))

        if cmd == "acc":
            acc += arg
            line_to_read += 1
        elif cmd == "nop":
            line_to_read += 1
        elif cmd == "jmp":
            line_to_read += arg

    return acc, infinite


def main():
    lines = read("8_1.txt")

    print(run(lines))

    for i, line in enumerate(lines):
        if "jmp" in line or "nop" in line:
            new_lines = lines.copy()
            if "jmp" in line:
                new_lines[i] = line.replace("jmp", "nop")
            else:
                new_lines[i] = line.replace("nop", "jmp")

            acc, infinite = run(new_lines)

            if not infinite:
                print(acc)




if __name__ == '__main__':
    main()
