from typing import List

file = open('input3.txt')
line = file.readline().strip()

diagnostic: List[str] = []
oxygen_gen: int = -1
oxygen_list: List[str] = []
co2_scrubber: int = -1
co2_list: List[str] = []

oxygen_occurrences: List[int] = [0, 0]
co2_occurrences: List[int] = [0, 0]

while line:
    diagnostic.append(line)
    line = file.readline().strip()
file.close()

oxygen_list = diagnostic.copy()
co2_list = diagnostic.copy()


def get_occurrences(my_list: List[str], index: int) -> List[int]:
    new_occurrences: List[int] = [0, 0]
    for item in my_list:
        new_occurrences[int(item[index])] += 1
    return new_occurrences


def purge_list(my_list: List[str], criteria: str, index: int) -> List[str]:
    if len(my_list) == 1:
        return my_list
    new_list: List[str] = my_list.copy()
    for item in my_list:
        if item[index] != criteria:
            new_list.remove(item)

    return new_list


for i in range(len(diagnostic[0])):
    oxygen_occurrences = get_occurrences(oxygen_list.copy(), i)
    co2_occurrences = get_occurrences(co2_list.copy(), i)
    if oxygen_occurrences[0] > oxygen_occurrences[1]:
        oxygen_list = purge_list(oxygen_list.copy(), '0', i)
    else:
        oxygen_list = purge_list(oxygen_list.copy(), '1', i)
    if co2_occurrences[0] > co2_occurrences[1]:
        co2_list = purge_list(co2_list.copy(), '1', i)
    else:
        co2_list = purge_list(co2_list.copy(), '0', i)

oxygen_gen = int(oxygen_list[0], 2)
co2_scrubber = int(co2_list[0], 2)

life_support: int = oxygen_gen * co2_scrubber

print("ANSWER = {0}".format(life_support))
