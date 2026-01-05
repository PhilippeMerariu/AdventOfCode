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
        if self.x == value.x and self.y == value.y and self.z == value.z:
            return True
        return False

    def __repr__(self) -> str:
        return f"Box{self.id}({self.x}, {self.y}, {self.z})"

connections = []
count = 1

def get_box(id: int) -> Box:
    for box in flatten_connections():
        if box.id == id:
            return box
    raise Exception("No box found")

def box_dist(b1: Box, b2: Box) -> float:
    return math.sqrt((b2.x - b1.x)**2 + (b2.y - b1.y)**2 + (b2.z - b1.z)**2)

while line:
    line = line.strip('\n')
    coords = line.split(',')
    x, y, z = int(coords[0]), int(coords[1]), int(coords[2])
    connections.append([Box(count, x, y, z)])
    count += 1
    line = file.readline()
file.close()

def flatten_connections() -> list:
    flat_conn = []
    for conn in connections:
        flat_conn += conn
    return flat_conn

dists = {}
for opt in list(itertools.combinations(flatten_connections(), 2)):
    box1: Box = opt[0]
    box2: Box = opt[1]
    dists.update({(box1.id, box2.id): box_dist(box1, box2)})

def get_min(dists: dict) -> tuple[Box, Box]:
    min_dist = math.inf
    min_pair = (0, 0)
    for pair, d in dists.items():
        if d < min_dist:
            min_dist = d
            min_pair = pair
    box1, box2 = get_box(min_pair[0]), get_box(min_pair[1])
    dists.pop(min_pair)
    return (box1, box2)

def is_alone(box: Box) -> bool:
    for conn in connections:
        if box in conn:
            return len(conn) == 1
    raise Exception(f"{box} not found in connections")

def remove_single_box(box: Box) -> None:
    for conn in connections:
        if box in conn and len(conn) == 1:
            connections.remove(conn)
            return

def connect(single_box: Box, connected_box: Box) -> None:
    for conn in connections:
        if connected_box in conn:
            conn.append(single_box)
            return

def connect_many(box1: Box, box2: Box) -> None:
    box1_conn = []
    for conn in connections:
        if box1 in conn:
            box1_conn = conn
            break
    if box2 in box1_conn:
        return
    for conn in connections:
        if box2 in conn:
            box1_conn += conn
            connections.remove(conn)
            return

def make_connection(box1: Box, box2: Box) -> bool:
    box1_alone = is_alone(box1)
    box2_alone = is_alone(box2)
    if box1_alone and box2_alone:
        connections.insert(0, [box1, box2])
        remove_single_box(box1)
        remove_single_box(box2)
        return True
    if not box1_alone and not box2_alone:
        connect_many(box1, box2)
        return True
    if box1_alone:
        connect(box1, box2)
        remove_single_box(box1)
        return True
    if box2_alone:
        connect(box2, box1)
        remove_single_box(box2)
    return False


nb_connections = 1000
for _ in range(nb_connections):
    box1, box2 = get_min(dists)
    make_connection(box1, box2)

connection_sizes = [len(conn) for conn in connections]
connection_sizes.sort(reverse=True)

result = connection_sizes[0] * connection_sizes[1] * connection_sizes[3]

print(f"ANSWER = {result}")
