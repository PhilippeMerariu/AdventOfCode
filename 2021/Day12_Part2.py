from typing import List, Dict

connections: Dict[str, List[str]] = {}
paths: List[List[str]] = []
small_caves: List[str] = []

file = open('input12.txt')
line = file.readline().strip()


def update_connections(key, val) -> None:
    if key == 'end':
        return
    if val == 'start':
        return
    if key not in connections:
        connections.update({key: [val]})
    else:
        arr: List[str] = connections.get(key)
        arr.append(val)
        connections.update({key: arr.copy()})


def path_ok(path: List[str]) -> bool:
    count: int = 0
    for small in small_caves:
        nb_repeats: int = len([x for x in path if x == small])
        if  nb_repeats > 1:
            count += nb_repeats/2
            if count > 1:
                return False
    return True


while line:
    input_caves: List[str] = line.split("-")
    update_connections(input_caves[0], input_caves[1])
    update_connections(input_caves[1], input_caves[0])
    if input_caves[0].islower() and input_caves[0] not in ['start', 'end'] and input_caves[0] not in small_caves:
        small_caves.append(input_caves[0])
    if input_caves[1].islower() and input_caves[1] not in ['start', 'end'] and input_caves[1] not in small_caves:
        small_caves.append(input_caves[1])
    line = file.readline().strip()
file.close()

for starting_path in connections.get('start'):
    paths.append(['start', starting_path])

answer: int = 0

while not all(x[-1] == 'end' for x in paths):
    for p in paths.copy():
        if p[-1] == 'end':
            continue
        next_options: List[str] = connections.get(p[-1])
        paths.remove(p)
        for opt in next_options:
            new_path: List[str] = p.copy()
            new_path.append(opt)
            if path_ok(new_path) and new_path not in paths:
                if new_path[-1] == 'end':
                    answer += 1
                else:
                    paths.append(new_path.copy())

print("ANSWER = {0}".format(answer))
