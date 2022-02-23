from typing import Dict, List

STEPS: int = 10
pattern: str = ""
polymer_rules: Dict[str, str] = {}

file = open('input14.txt')
line = file.readline()

while line:
    if not pattern:
        pattern = line.strip()
    elif line == "\n":
        line = file.readline()
        continue
    else:
        rule: List[str] = line.strip().split(" -> ")
        polymer_rules.update({rule[0]: rule[1]})
    line = file.readline()
file.close()

for _ in range(STEPS):
    pattern_copy: str = pattern
    for i in range(len(pattern_copy)):
        try:
            pair: str = pattern_copy[i] + pattern_copy[i + 1]
            new_element: str = polymer_rules.get(pair)
            new_element_index: int = i + (i + 1)
            pattern = pattern[:new_element_index] + new_element + pattern[new_element_index:]
        except IndexError:
            pass

unique_elements: List[str] = list(set(pattern))
element_occurrence: Dict[str, int] = {}

for elem in unique_elements:
    element_occurrence.update({elem: pattern.count(elem)})

most_occurring_elem: str = max(element_occurrence, key=element_occurrence.get)
least_occurring_elem: str = min(element_occurrence, key=element_occurrence.get)

answer: int = element_occurrence.get(most_occurring_elem) - element_occurrence.get(least_occurring_elem)
print("ANSWER = {0}".format(answer))
