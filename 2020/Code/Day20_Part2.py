import math
from typing import List, Dict

tiles_orig: Dict[int, List[str]] = {}
tiles_final: Dict[int, List[str]] = {}
grid: List[List[int]] = []
matched: List[int] = []
links: Dict[int, List[int]] = {}


def get_tile_number(s: str) -> int:
    arr = s.split(" ")
    nb = arr[1]
    return int(nb[:-2])


file = open('input20_test.txt')
line = file.readline()

tile_nb: int = 0
tile_piece: List[str] = []

while line:
    if line.startswith("Tile"):
        tile_nb = get_tile_number(line)
    elif line == "\n":
        tiles_orig.update({tile_nb: tile_piece.copy()})
        tile_piece.clear()
    else:
        line = line.strip()
        tile_piece.append(line)
    line = file.readline()

tiles_orig.update({tile_nb: tile_piece.copy()})
tile_piece.clear()

file.close()

tiles_final = tiles_orig.copy()

# init empty grid
grid_size: int = int(math.sqrt(len(tiles_orig)))
column: List[int] = []
for i in range(grid_size):
    for j in range(grid_size):
        column.append(0)
    grid.append(column.copy())
    column.clear()


def rotate_cw(piece: List[str]) -> List[str]:
    new_line: str = ""
    new_piece: List[str] = []
    for col in range(len(piece[0])):
        for row in range(len(piece) - 1, -1, -1):
            new_line = new_line + piece[row][col]
        new_piece.append(new_line)
        new_line = ""
    return new_piece


def flip(piece: List[str]) -> List[str]:
    new_piece: List[str] = []
    for row in range(len(piece)):
        new_line = piece[row][::-1]
        new_piece.append(new_line)
    return new_piece


def add_to_grid(start_tile: int, new_tile: int, position: str):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == start_tile:
                if position == "bottom":
                    grid[i + 1][j] = new_tile
                else:
                    grid[i][j + 1] = new_tile


def compare(p1: str, p2: str) -> bool:
    return p1 == p2


def compare_side(right: List[str], left: List[str]) -> bool:
    right_side: str = ""
    left_side: str = ""
    for r in right:
        right_side += r[-1]
    for l in left:
        left_side += l[0]
    return right_side == left_side


def find_top_match(index: int, piece: List[str]):
    top: str = piece[0]
    for t in tiles_orig:
        if t == index:
            continue
        other_piece: List[str] = tiles_orig.get(t)
        for _ in range(4):
            for _ in range(2):
                if compare(top, other_piece[len(other_piece) - 1]):
                    matched.append(t)
                    tiles_final.update({t: other_piece})
                other_piece = flip(other_piece)
            other_piece = rotate_cw(other_piece)


def find_bottom_match(index: int, piece: List[str], options: List[int]) -> bool:
    bottom: str = piece[-1]
    for t in options:
        if t == index:
            continue
        other_piece: List[str] = tiles_final.get(t)
        for _ in range(4):
            for _ in range(2):
                if compare(bottom, other_piece[0]):
                    if t not in matched:
                        matched.append(t)
                    tiles_final.update({t: other_piece})
                    add_to_grid(index, t, "bottom")
                    return True
                other_piece = flip(other_piece)
            other_piece = rotate_cw(other_piece)
    print("no bottom match found -> {0}".format(index))
    return False


def find_right_match(index: int, piece: List[str], options: List[int]) -> bool:
    right: str = rotate_cw(rotate_cw(rotate_cw(piece)))[0]
    for t in options:
        if t == index:
            continue
        other_piece: List[str] = tiles_final.get(t)
        for _ in range(4):
            for _ in range(2):
                if compare_side(piece, other_piece):
                    if t not in matched:
                        matched.append(t)
                    tiles_final.update({t: other_piece})
                    add_to_grid(index, t, "right")
                    return True
                other_piece = flip(other_piece)
            other_piece = rotate_cw(other_piece)
    print("no right match found -> {0}".format(index))
    return False


def find_all_matches():
    for t in tiles_orig:
        piece = tiles_orig.get(t)
        for _ in range(4):
            for _ in range(2):
                find_top_match(t, piece)
                piece = flip(piece)
            piece = rotate_cw(piece)

        links.update({t: matched.copy()})
        matched.clear()


find_all_matches()

corner_tiles = []
border_tiles = []
middle_tiles = []

# remove duplicates
for index in links:
    link = links.get(index)
    temp = link.copy()
    link.clear()
    for x in temp:
        if x not in link:
            link.append(x)
    if len(link) == 2:
        corner_tiles.append(index)
    elif len(link) == 3:
        border_tiles.append(index)
    else:
        middle_tiles.append(index)

print("# Corners = {0}".format(len(corner_tiles)))
print("# Borders = {0}".format(len(border_tiles)))
print("# Middles = {0}".format(len(middle_tiles)))
print()

# fix top-right corner piece
# rotate all other pieces to match to it
grid[0][0] = corner_tiles[0]
matched.clear()
matched.append(corner_tiles[0])

# find position of all tiles
for tile in matched:
    piece = tiles_final.get(tile)
    find_bottom_match(tile, piece, links.get(tile))
    find_right_match(tile, piece, links.get(tile))

print("\nGRID IDs:")
for g in grid:
    print(g)

# remove borders of all tiles
for tile_id in tiles_final:
    tile = tiles_final.get(tile_id)[1:-1]
    new_tile: List[str] = []
    for line in tile:
        new_tile.append(line[1:-1])
    tiles_final.update({tile_id: new_tile})


def join_rows(row: List[int]) -> List[str]:
    full_grid: List[str] = []
    for _ in range(len(list(tiles_final.values())[0][0])):
        full_grid.append("")
    for r in row:
        piece = tiles_final.get(r)
        for j in range(len(piece)):
            full_grid[j] += piece[j]
    return full_grid


# print final picture
print("\nPICTURE:")
picture: List[List[str]] = []
for g in grid:
    picture.append(join_rows(g))
for pic in picture:
    for r in pic:
        print(r)
