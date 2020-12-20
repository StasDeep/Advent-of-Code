import numpy as np

from utils import read, p1, p2


def main():
    tiles = {
        int(tile.split("\n")[0].split()[-1][:-1]):
        np.array([list(line) for line in tile.split("\n")[1:]]) == "#"
        for tile in "\n".join(read()).split("\n\n")
    }

    width = int(np.sqrt(len(tiles)))

    for start_tile_num in tiles:
        for start_tile in orientations(tiles[start_tile_num]):
            combined_tiles = [(start_tile_num, start_tile)]
            used = {start_tile_num}
            found_all_matches = True
            for i in range(1, len(tiles)):
                found_match = False
                for tile_num, tile in tiles.items():
                    if tile_num in used:
                        continue

                    prev_htile = combined_tiles[i - 1][1] if i % width != 0 else None
                    prev_vtile = combined_tiles[i - width][1] if i // width != 0 else None

                    for try_tile in orientations(tile):
                        if prev_htile is not None and not np.all(prev_htile[:, -1] == try_tile[:, 0]):
                            continue
                        if prev_vtile is not None and not np.all(prev_vtile[-1, :] == try_tile[0, :]):
                            continue

                        combined_tiles.append((tile_num, try_tile))
                        used.add(tile_num)
                        found_match = True
                        break

                if not found_match:
                    # If there wasn't any match found after checking all tiles,
                    # stop going to the next positions, because it is not possible to
                    # match everything with this starting tile
                    found_all_matches = False
                    break
            if found_all_matches:
                break
        if found_all_matches:
            break

    tile_nums = np.array([x[0] for x in combined_tiles]).reshape((width, width))
    p1(tile_nums[0, 0] * tile_nums[0, -1] * tile_nums[-1, -1] * tile_nums[-1, 0])

    sq_width = combined_tiles[0][1].shape[0] - 2
    full_img = np.zeros((sq_width * width, sq_width * width), dtype=bool)
    for idx, (_, tile) in enumerate(combined_tiles):
        i, j = divmod(idx, width)
        full_img[i*sq_width:i*sq_width+sq_width, j*sq_width:j*sq_width+sq_width] = tile[1:-1, 1:-1]

    monster = (
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    )
    monster = np.array([list(line) for line in monster]) == "#"

    for img in orientations(full_img):
        num_monsters = 0

        for i in range(full_img.shape[0] - monster.shape[0] + 1):
            for j in range(full_img.shape[1] - monster.shape[1] + 1):
                img_slice = img[i:i + monster.shape[0], j:j + monster.shape[1]]
                if np.all((img_slice & monster) == monster):
                    num_monsters += 1

        if num_monsters > 0:
            p2(np.sum(full_img) - num_monsters * np.sum(monster))
            return


def orientations(arr):
    for rot in range(4):
        for flip in range(4):
            new_arr = np.rot90(arr, k=rot)
            new_arr = flip_arr(new_arr, flip)
            yield new_arr


def flip_arr(arr, num):
    if num == 1:
        return np.flip(arr, 0)
    elif num == 2:
        return np.flip(arr, 1)
    elif num == 3:
        return np.flip(arr)
    else:
        return arr
