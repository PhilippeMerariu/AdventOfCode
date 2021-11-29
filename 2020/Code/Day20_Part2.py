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


def compare(p1: str, p2: str) -> bool:
    return p1 == p2


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
                other_piece = flip(other_piece)
            other_piece = rotate_cw(other_piece)


def find_all_matches():
    res = False
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

print("Corner = {0}".format(len(corner_tiles)))
print("Border = {0}".format(len(border_tiles)))
print("Middle = {0}".format(len(middle_tiles)))

# fix top-right corner piece
# rotate all other pieces to match to it


