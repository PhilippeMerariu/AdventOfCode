from typing import List, Dict

import numpy
from scipy.stats import stats

file = open('input7.txt')
line = file.readline().strip()

crab_list: List[int] = [int(x) for x in line.split(",")]
crabs: Dict[int, int] = {}  # pos, count

for i in crab_list:
    nb_crabs: int = len([x for x in crab_list if x == i])
    crabs.update({i: nb_crabs})

file.close()

mean: int = round(sum(crab_list) / len(crab_list))
median: int = round(numpy.median(crab_list))
mode: int = stats.mode(crab_list)


def calculate_fuel(nb: int) -> int:
    fuel: int = 0
    for pos, count in crabs.items():
        temp_fuel: int = 0
        diff: int = abs(nb - pos)
        for i in range(1, diff + 1):
            temp_fuel += i
        fuel += temp_fuel * count
    return fuel


all_fuel_values: List[int] = []
for i in range(min(crab_list), max(crab_list)+1):
    all_fuel_values.append(calculate_fuel(i))

answer: int = min(all_fuel_values)

print("\nANSWER = {0}".format(answer))
