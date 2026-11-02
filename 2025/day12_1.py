file = open('input12.txt')
content = file.read()
file.close()

shapes = []
regions = []

# the file has one blank-line-separated block per shape, then a final
# block holding every region. a shape block starts with a header like "0:",
# a region line looks like "12x5: 1 0 1 0 2 2"
for block in content.split('\n\n'):
    lines = [line for line in block.split('\n') if line]
    if not lines:
        continue
    if lines[0].endswith(':'):
        shapes.append(lines[1:])
    else:
        for line in lines:
            size, quantities = line.split(':')
            width, length = size.split('x')
            regions.append((int(width), int(length), [int(q) for q in quantities.split()]))


def read_cells(picture):
    # a shape is just the list of (row, col) spots where it has a '#'
    return [(r, c) for r, row in enumerate(picture) for c, ch in enumerate(row) if ch == '#']

def normalize(cells):
    # slide the shape up and left until it touches row 0 and column 0, and
    # sort it, so two shapes that are the same look the same
    top = min(r for r, c in cells)
    left = min(c for r, c in cells)
    return tuple(sorted((r - top, c - left) for r, c in cells))

def rotate(cells):
    # quarter turn clockwise: a cell at (row, col) moves to (col, -row)
    return [(c, -r) for r, c in cells]

def flip(cells):
    # mirror left-to-right: (row, col) moves to (row, -col)
    return [(r, -c) for r, c in cells]

def all_orientations(picture):
    # a present can be rotated and flipped, which gives at most 8 versions:
    # 4 rotations, and the mirror of each of those. normalizing lets a set
    # throw away the duplicates for shapes that are already symmetric
    cells = read_cells(picture)
    found = set()
    for _ in range(4):
        found.add(normalize(cells))
        found.add(normalize(flip(cells)))
        cells = rotate(cells)
    return sorted(found)


orientations_of = [all_orientations(picture) for picture in shapes]
cells_in = [len(read_cells(picture)) for picture in shapes]


def search(width, length, quantities):
    # walk the region one cell at a time, reading left-to-right then top-to-bottom.
    # at each cell we either start a present whose own first cell sits exactly
    # here, or we decide this cell stays empty and move on. anchoring presents by
    # their first cell means we never have to look backwards, so every possible
    # packing gets built exactly once.
    taken = set()

    def place(cell_index, left, needed, available):
        if needed == 0:
            return True          # every present found a home
        if needed > available:
            return False         # not enough room left, no point going deeper

        row, col = divmod(cell_index, width)
        if (row, col) in taken:
            return place(cell_index + 1, left, needed, available)

        for shape, count in enumerate(left):
            if count == 0:
                continue
            rest = left[:shape] + (count - 1,) + left[shape + 1:]
            for orientation in orientations_of[shape]:
                # orientation[0] is its topmost-then-leftmost cell; shift the
                # whole shape so that cell lands on (row, col)
                offset = orientation[0][1]
                cells = [(row + r, col + c - offset) for r, c in orientation]
                if all(0 <= r < length and 0 <= c < width and (r, c) not in taken
                       for r, c in cells):
                    taken.update(cells)
                    if place(cell_index + 1, rest, needed - cells_in[shape],
                             available - cells_in[shape]):
                        return True
                    taken.difference_update(cells)

        # leave this cell empty, so one less cell is available from here on
        return place(cell_index + 1, left, needed, available - 1)

    total = sum(cells_in[shape] * n for shape, n in enumerate(quantities))
    return place(0, tuple(quantities), total, width * length)


result = 0

for width, length, quantities in regions:
    needed = sum(cells_in[shape] * n for shape, n in enumerate(quantities))
    presents = sum(quantities)

    if needed > width * length:
        # the presents cover more squares than the region even has
        fits = False
    elif presents <= (width // 3) * (length // 3):
        # every shape is drawn inside a 3x3 box, so if we can cut that many
        # 3x3 blocks out of the region each present can have a block to itself
        fits = True
    else:
        # neither shortcut decides it, so actually try to pack the region
        fits = search(width, length, quantities)

    if fits:
        result += 1

print(f"ANSWER = {result}")
