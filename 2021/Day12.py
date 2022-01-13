from typing import List, Dict

caves: List[str] = []
start_caves: List[str] = []
end_caves: List[str] = []

connections: Dict[str, List[str]] = {}

file = open('input12_test.txt')
line = file.readline().strip()

while line:
    input_caves: List[str] = line.split("-")
    if input_caves[0] not in connections:
        connections.update({input_caves[0]: [input_caves[1]]})
    else:
        connections.update({input_caves[0]: connections.get(input_caves[0]).append(input_caves[1])})

    if input_caves[1] not in connections:
        connections.update({input_caves[1]: [input_caves[0]]})
    else:
        connections.update({input_caves[1]: connections.get(input_caves[1]).append(input_caves[0])})
    line = file.readline().strip()
file.close()





answer: int = 0
print("ANSWER = {0}".format(answer))
