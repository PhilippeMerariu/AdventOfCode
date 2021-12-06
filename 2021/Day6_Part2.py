from typing import List, Dict

NEW_FISH_DAYS: int = 8
FISH_DAYS: int = 6
NB_OF_DAYS: int = 256

file = open('input6.txt')
line = file.readline().strip()

fish: List[int] = [int(x) for x in line.split(",")]

file.close()

fish_counter: Dict[int, int] = {}
new_fish_counter: Dict[int, int] = {}


def clear_new_fish_counter():
    for i in new_fish_counter:
        new_fish_counter[i] = 0


for i in range(NEW_FISH_DAYS + 1):
    nb_fish: int = len([int(x) for x in fish if x == i])
    fish_counter.update({i: nb_fish})
    new_fish_counter.update({i: 0})

days: int = 0
for days in range(NB_OF_DAYS):
    for nb_days, nb_fish in fish_counter.items():
        if nb_days == 0:
            new_fish_counter[NEW_FISH_DAYS] += nb_fish
            new_fish_counter[FISH_DAYS] += nb_fish
        else:
            new_fish_counter[nb_days - 1] += nb_fish
    fish_counter = new_fish_counter.copy()
    clear_new_fish_counter()

answer: int = sum(fish_counter.values())

print("ANSWER = {0}".format(answer))
