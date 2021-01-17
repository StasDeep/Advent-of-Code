from itertools import product

from utils import read, p1, p2


def main():
    lines = read()

    memory = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[-1]
        else:
            mem_idx = int(line.split(' = ')[0].split('[')[-1][:-1])
            num = int(line.split(' = ')[-1])

            bin_num = bin(num)[2:].zfill(36)
            new_num = []
            for mask_bit, bit in zip(mask, bin_num):
                if mask_bit == 'X':
                    new_num.append(bit)
                else:
                    new_num.append(mask_bit)

            memory[mem_idx] = int(''.join(new_num), 2)

    p1(sum(memory.values()))

    memory = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[-1]
        else:
            mem_idx = int(line.split(' = ')[0].split('[')[-1][:-1])
            num = int(line.split(' = ')[-1])

            bin_num = bin(mem_idx)[2:].zfill(36)
            new_idx = []
            for mask_bit, bit in zip(mask, bin_num):
                if mask_bit == '0':
                    new_idx.append(bit)
                elif mask_bit == '1':
                    new_idx.append(mask_bit)
                else:
                    new_idx.append('X')

            x_indices = [i for i, x in enumerate(new_idx) if x == 'X']
            all_indices = []
            for values in product(['0', '1'], repeat=len(x_indices)):
                cur_idx = new_idx.copy()
                for i, idx in enumerate(x_indices):
                    cur_idx[idx] = values[i]

                all_indices.append(cur_idx)

            for idx in all_indices:
                memory[int(''.join(idx), 2)] = num

    p2(sum(memory.values()))
