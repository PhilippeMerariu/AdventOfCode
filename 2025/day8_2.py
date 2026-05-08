import math

import itertools

file = open('input8.txt')
line = file.readline()

result = 0

class Box:
    def __init__(self, id: int, x: int, y: int, z: int):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, value) -> bool:
        return self.id == value.id

    def __repr__(self) -> str:
        return f"Box{self.id}({self.x}, {self.y}, {self.z})"

all_boxes = []
count = 1

def get_box(id: int) -> Box:
    for box in all_boxes:
        if box.id == id:
            return box
    raise Exception("No box found")

def box_dist(b1: Box, b2: Box) -> float:
    return math.sqrt((b2.x - b1.x)**2 + (b2.y - b1.y)**2 + (b2.z - b1.z)**2)

while line:
    line = line.strip('\n')
    coords = line.split(',')
    x, y, z = int(coords[0]), int(coords[1]), int(coords[2])
    all_boxes.append(Box(count, x, y, z))
    count += 1
    line = file.readline()
file.close()

group_map = {box.id: [box] for box in all_boxes}
unique_circuits = {id(v): v for v in group_map.values()}

dists = {}
for opt in list(itertools.combinations(all_boxes, 2)):
    box1: Box = opt[0]
    box2: Box = opt[1]
    dists.update({(box1.id, box2.id): box_dist(box1, box2)})

sorted_dists = dict(sorted(dists.items(), key=lambda item: item[1]))

def make_connection(box1: Box, box2: Box) -> bool:
    group1 = group_map[box1.id]
    group2 = group_map[box2.id]

    if group1 == group2:
        return False

    for box in group2:
        group1.append(box)
        group_map[box.id] = group1

    if id(group2) in unique_circuits:
        del unique_circuits[id(group2)]

    return True

for i in range(len(sorted_dists)):
    box_id1, box_id2 = list(sorted_dists.keys())[i]
    box1, box2 = get_box(box_id1), get_box(box_id2)
    print(f"Progress: {i}/{len(sorted_dists)} || # Connections: {len(unique_circuits)}", end="\r", flush=True)
    if make_connection(box1, box2):
        if len(unique_circuits) == 1:
            result = box1.x * box2.x
            print()
            break

print(f"ANSWER = {result}")
