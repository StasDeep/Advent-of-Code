import numpy as np

from utils import read, p1, p2


def main():
    tiles = "\n".join(read()).split("\n\n")

    tiles = {
        int(tile.split("\n")[0].split()[-1][:-1]):
        np.array([list(line) for line in tile.split("\n")[1:]]) == "#"
        for tile in tiles
    }

    width = int(np.sqrt(len(tiles)))

    for stile_num in tiles:
        for rot in range(4):
            for flip in range(4):
                idxs = np.zeros((width, width), dtype=int)
                rots = np.zeros((width, width), dtype=int)
                flips = np.zeros((width, width), dtype=int)
                idxs[0, 0] = stile_num
                flips[0, 0] = flip
                rots[0, 0] = rot
                used = {stile_num}
                for i in range(1, len(tiles)):
                    y, x = divmod(i, width)
                    for tile_num, tile in tiles.items():
                        if tile_num in used:
                            continue

                        check_hor = not x == 0
                        check_vert = not y == 0

                        if check_hor:
                            prev_hor_tile = tiles[idxs[divmod(i-1, width)]]
                            prev_rot = rots[divmod(i - 1, width)]
                            prev_flip = flips[divmod(i - 1, width)]
                            prev_hor_tile = flip_arr(prev_hor_tile, prev_flip)
                            prev_hor_tile = np.rot90(prev_hor_tile, k=prev_rot)

                        if check_vert:
                            prev_vert_tile = tiles[idxs[divmod(i - width, width)]]
                            prev_rot = rots[divmod(i - width, width)]
                            prev_flip = flips[divmod(i - width, width)]
                            prev_vert_tile = flip_arr(prev_vert_tile, prev_flip)
                            prev_vert_tile = np.rot90(prev_vert_tile, k=prev_rot)

                        for try_rot in range(4):
                            for try_flip in range(4):
                                tile_flipped = flip_arr(tile, try_flip)
                                tile_rotated = np.rot90(tile_flipped, k=try_rot)
                                if check_hor:
                                    if not np.all(prev_hor_tile[:, -1] == tile_rotated[:, 0]):
                                        continue
                                if check_vert:
                                    if not np.all(prev_vert_tile[-1, :] == tile_rotated[0, :]):
                                        continue

                                idxs[y, x] = tile_num
                                rots[y, x] = try_rot
                                flips[y, x] = try_flip
                                break

                            if idxs[y, x] != 0:
                                break

                        if idxs[y, x] != 0:
                            used.add(tile_num)
                            break

                    if idxs[y, x] == 0:
                        break

                if np.all(idxs) != 0:
                    break

            if np.all(idxs) != 0:
                break

        if np.all(idxs) != 0:
            break

    p1(idxs[0, 0] * idxs[0, -1] * idxs[-1, -1] * idxs[-1, 0])

    sq_width = tiles[idxs[0, 0]].shape[0] - 2
    full_img = np.zeros((sq_width * width, sq_width * width), dtype=bool)
    for (i, j), tile_num in np.ndenumerate(idxs):
        rot = rots[i, j]
        flip = flips[i, j]
        tile = tiles[tile_num]
        tile = flip_arr(tile, flip)
        tile = np.rot90(tile, k=rot)
        full_img[i*sq_width:i*sq_width+sq_width, j*sq_width:j*sq_width+sq_width] = tile[1:-1, 1:-1]

    sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    sea_monster = np.array([list(line) for line in sea_monster.split("\n")]) == "#"
    for row in sea_monster:
        print("".join("#" if x else " " for x in row))

    for rot in range(4):
        for flip in range(4):
            img = np.rot90(full_img, k=rot)
            img = flip_arr(img, flip)
            monster_num = 0
            if rot == 3 and flip == 2:
                print("l")

            for i in range(full_img.shape[0] - sea_monster.shape[0] + 1):
                for j in range(full_img.shape[1] - sea_monster.shape[1] + 1):
                    img_slice = img[i:i+ sea_monster.shape[0], j:j+sea_monster.shape[1]]
                    if np.all((img_slice & sea_monster) == sea_monster):
                        monster_num += 1

            if monster_num > 0:
                p2(np.sum(full_img) - monster_num * np.sum(sea_monster))
                return


def flip_arr(arr, num):
    if num == 1:
        arr = np.flip(arr, 0)
    elif num == 2:
        arr = np.flip(arr, 1)
    elif num == 3:
        arr = np.flip(arr)
    return arr
