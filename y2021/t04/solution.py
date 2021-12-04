from utils import read, p1, p2


def main():
    lines = read()

    nums, *boards_raw = '\n'.join(lines).split('\n\n')
    nums = list(map(int, nums.split(',')))
    boards = []

    for b in boards_raw:
        boards.append(list(map(int, b.split())))

    idxs = [set() for _ in boards]

    valid_seqs = [
        {0+i*5, 1+i*5, 2+i*5, 3+i*5, 4+i*5} for i in range(5)
    ] + [
        {0+i, 5+i, 10+i, 15+i, 20+i} for i in range(5)
    ]

    boards_won = []

    for num in nums:
        for i, board in enumerate(boards):
            if i in boards_won:
                continue
            if num not in board:
                continue
            idx = board.index(num)
            idxs[i].add(idx)

            for valid_seq in valid_seqs:
                if len(idxs[i].intersection(valid_seq)) == 5:
                    if not boards_won:
                        p1(sum(board[j] for j in range(25) if j not in idxs[i]) * num)
                    boards_won.append(i)

                    if len(boards_won) == len(boards):
                        p2(sum(board[j] for j in range(25) if j not in idxs[i]) * num)
                    break
