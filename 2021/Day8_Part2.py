from typing import List, Dict

UNIQUE_VALUES: List[int] = [2, 3, 4, 7]
LETTERS: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
NUMBER_SEGMENTS: Dict[int, int] = {0: 6,
                                   1: 2,
                                   2: 5,
                                   3: 5,
                                   4: 4,
                                   5: 5,
                                   6: 6,
                                   7: 3,
                                   8: 7,
                                   9: 6}

NUMBERS: Dict[int, List[str]] = {0: ['a', 'b', 'c', 'e', 'f', 'g'],
                                 1: ['c', 'f'],
                                 2: ['a', 'c', 'd', 'e', 'g'],
                                 3: ['a', 'c', 'd', 'f', 'g'],
                                 4: ['b', 'c', 'd', 'f'],
                                 5: ['a', 'b', 'd', 'f', 'g'],
                                 6: ['a', 'b', 'd', 'e', 'f', 'g'],
                                 7: ['a', 'c', 'f'],
                                 8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                                 9: ['a', 'b', 'c', 'd', 'f', 'g']}

file = open('input8.txt')
line = file.readline().strip()

inputs: Dict[int, List[str]] = {}
outputs: Dict[int, List[str]] = {}

segments: Dict[str, str] = {}


def reset_segment():
    for char in LETTERS:
        segments.update({char: ''})


reset_segment()
count: int = 0

while line:
    in_out: List[str] = line.split(" | ")
    inputs.update({count: in_out[0].split(" ")})
    outputs.update({count: in_out[1].split(" ")})
    count += 1
    line = file.readline().strip()
file.close()


def is_in_segment(letter: str) -> bool:
    for orig, value in segments.items():
        if value == letter:
            return True
    return False


def find_top_bar(seven: List[str], one: List[str]):
    for s in seven[0]:
        if s not in one[0]:
            segments.update({'a': s})
            return


def find_right_bars(options: List[str], one: List[str]):
    # find number 6
    for opt in options:
        if not (one[0][0] in opt and one[0][1] in opt):
            for letter in LETTERS:
                if letter not in opt:
                    segments.update({'c': letter})
                    segments.update({'f': one[0][0] if letter == one[0][1] else one[0][1]})
            return


def find_middle_left_and_bottom_bars(options: List[str], four: List[str]):
    # find number 3
    right_segments: List[str] = [segments.get('c'), segments.get('f')]
    for opt in options:
        if right_segments[0] in opt and right_segments[1] in opt:
            for f in four[0]:
                if f in opt and f not in right_segments:
                    segments.update({'d': f})
                elif f not in right_segments and f not in opt:
                    segments.update({'b': f})
            for o in opt:
                if o not in four[0] and not is_in_segment(o):
                    segments.update({'g': o})
                    break
            find_last_segment()
            return


def find_last_segment():
    found: List[str] = []
    missing: str = ''
    for seg, value in segments.items():
        if value == "":
            missing = seg
        else:
            found.append(value)
    for char in LETTERS:
        if char not in found:
            segments.update({missing: char})
            return


def rewire_sequence(sequence: str) -> str:
    rewired: str = ''
    for s in sequence:
        for orig, mapped in segments.items():
            if s == mapped:
                rewired += orig
    return rewired


def find_number(sequences: List[str]) -> int:
    nb: str = ''
    for sequence in sequences:
        if len(sequence) == 2:
            nb += "1"
        elif len(sequence) == 3:
            nb += "7"
        elif len(sequence) == 4:
            nb += "4"
        elif len(sequence) == 7:
            nb += "8"
        else:
            sorted_converted_seq: List[str] = sorted(rewire_sequence(sequence))
            for n, chain in NUMBERS.items():
                if sorted_converted_seq == chain:
                    nb += str(n)
                    break
    return int(nb)


answer: List[int] = []

# split inputs by length
data: Dict[int, List[str]] = {}
for index, input in inputs.items():
    for val in input:
        data.update({len(val): [x for x in input if len(x) == len(val)]})
    find_top_bar(data.get(NUMBER_SEGMENTS.get(7)), data.get(NUMBER_SEGMENTS.get(1)))
    find_right_bars(data.get(6), data.get(NUMBER_SEGMENTS.get(1)))
    find_middle_left_and_bottom_bars(data.get(5), data.get(NUMBER_SEGMENTS.get(4)))
    answer.append(find_number(outputs.get(index)))
    reset_segment()

print("ANSWER = {0}".format(sum(answer)))
