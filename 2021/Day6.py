from typing import List

NEW_FISH_DAYS: int = 8
FISH_DAYS: int = 6
NB_OF_DAYS: int = 80

file = open('input6.txt')
line = file.readline().strip()

fish: List[int] = [int(x) for x in line.split(",")]

file.close()

baby_fish: List[int] = []

days: int = 0
while days < NB_OF_DAYS:
    for i in range(len(fish)):
        if fish[i] == 0:
            baby_fish.append(NEW_FISH_DAYS)
            fish[i] = FISH_DAYS
        else:
            fish[i] -= 1
    fish = fish + baby_fish.copy()
    baby_fish.clear()
    days += 1

answer: int = len(fish)


print("ANSWER = {0}".format(answer))
