import itertools

file = open('input9.txt')
line = file.readline()

result = 0

grid = []
corners = []
walls = []
inner_tiles = []

while line:
    line = line.strip('\n')
    corners.append(tuple(int(t) for t in line.split(',')))
    line = file.readline()
file.close()

# 2. Coordinate Compression
sorted_x = sorted(list(set(c[0] for c in corners)))
sorted_y = sorted(list(set(c[1] for c in corners)))

# Maps for fast lookup: coordinate -> index
x_map = {x: i for i, x in enumerate(sorted_x)}
y_map = {y: i for i, y in enumerate(sorted_y)}

# 3. Create a compressed grid (Boolean: Is this chunk inside the loop?)
# grid[i][j] represents the area between sorted_x[i]:sorted_x[i+1] and sorted_y[j]:sorted_y[j+1]
cols, rows = len(sorted_x), len(sorted_y)
is_filled = [[False for _ in range(rows)] for _ in range(cols)]

# Helper to mark the perimeter (Red/Green lines)
# This is much faster than storing every pixel
for i in range(len(corners)):
    p1 = corners[i]
    p2 = corners[(i + 1) % len(corners)]
    
    if p1[0] == p2[0]: # Vertical line
        x_idx = x_map[p1[0]]
        y_start, y_end = sorted( [y_map[p1[1]], y_map[p2[1]]] )
        for y_idx in range(y_start, y_end):
            # Mark edges if needed, but for 'inside' logic, 
            # we use the scanline/even-odd rule below.
            pass

# 4. Fill the interior using a Scanline (Even-Odd Rule)
# For each row of "chunks", determine which are inside the polygon
for j in range(rows - 1):
    y_mid = (sorted_y[j] + sorted_y[j+1]) / 2
    intersections = []
    for i in range(len(corners)):
        p1, p2 = corners[i], corners[(i + 1) % len(corners)]
        if min(p1[1], p2[1]) <= y_mid <= max(p1[1], p2[1]) and p1[1] != p2[1]:
            intersections.append(p1[0])
    
    intersections.sort()
    for start_x, end_x in zip(intersections[::2], intersections[1::2]):
        for i in range(x_map[start_x], x_map[end_x]):
            is_filled[i][j] = True

# 5. 2D Prefix Sum for O(1) Validation
# sum_table[i][j] = count of 'False' (empty) chunks in the rectangle from (0,0) to (i,j)
sum_table = [[0] * rows for _ in range(cols)]
for i in range(cols - 1):
    for j in range(rows - 1):
        val = 0 if is_filled[i][j] else 1
        sum_table[i+1][j+1] = val + sum_table[i][j+1] + sum_table[i+1][j] - sum_table[i][j]

def is_valid(x1, y1, x2, y2):
    # Get index bounds
    ix1, ix2 = sorted([x_map[x1], x_map[x2]])
    iy1, iy2 = sorted([y_map[y1], y_map[y2]])
    
    # Area of 'False' chunks in this range must be 0
    # Formula: Area = Table(BR) - Table(TR) - Table(BL) + Table(TL)
    empty_count = sum_table[ix2][iy2] - sum_table[ix1][iy2] - sum_table[ix2][iy1] + sum_table[ix1][iy1]
    return empty_count == 0

# 6. Check all red tile pairs
for (c1, c2) in itertools.combinations(corners, 2):
    if is_valid(c1[0], c1[1], c2[0], c2[1]):
        area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)
        if area > result:
            result = area

print(f"ANSWER = {result}")
