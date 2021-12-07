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
        fuel += abs(nb - pos) * count
    return fuel


mean_fuel: int = calculate_fuel(mean)
median_fuel: int = calculate_fuel(median)
mode_fuel: int = calculate_fuel(mode.mode[0])

print("MEAN: {0} -> FUEL: {1}".format(mean, mean_fuel))
print("MEDIAN: {0} -> FUEL: {1}".format(median, median_fuel))
print("MODE: {0} -> FUEL: {1}".format(mode.mode[0], mode_fuel))

answer: int = min(mean_fuel, median_fuel, mode_fuel)

print("\nANSWER = {0}".format(answer))
