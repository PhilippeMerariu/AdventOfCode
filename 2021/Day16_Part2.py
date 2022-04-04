from typing import List

SUM_ID: int = 0
PRODUCT_ID: int = 1
MIN_ID: int = 2
MAX_ID: int = 3
LITERAL_VALUE: int = 4
GREATER_ID: int = 5
LESS_ID: int = 6
EQUAL_ID: int = 7

OPERATORS: List[str] = ['+', '*', 'min', 'max', '>', '<', '=']

SUBPACKET_LENGTH: int = 0
NB_SUBPACKETS: int = 1

file = open('input16.txt')
line = file.readline().strip()

binary_str: str = str(bin(int(line, 16)))[2:]
while len(binary_str) % 4 != 0:
    binary_str = "0" + binary_str

version_sum: int = 0
subpacket_lengths: List[int] = []

values: List[int] = []
operations: List[int] = []

formula: List[str] = []


def subtract_length(val: int) -> None:
    for i in range(len(subpacket_lengths)):
        subpacket_lengths[i] -= val


def convert_operator(val: int) -> str:
    if val == SUM_ID:
        return '+'
    elif val == PRODUCT_ID:
        return '*'
    elif val == MIN_ID:
        return 'min'
    elif val == MAX_ID:
        return 'max'
    elif val == GREATER_ID:
        return '>'
    elif val == LESS_ID:
        return '<'
    elif val == EQUAL_ID:
        return '='


def get_numbers() -> List[int]:
    nbs: List[int] = []
    next_value: str = formula.pop(-1)
    while next_value not in OPERATORS:
        nbs.append(int(next_value))
        next_value = formula.pop(-1)
    formula.append(next_value)
    return nbs


def perform_operation() -> int:
    numbers: List[int] = get_numbers()
    operator: str = formula.pop(-1)
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        product: int = 1
        for nb in numbers:
            product *= nb
        return product
    elif operator == 'min':
        return min(numbers)
    elif operator == 'max':
        return max(numbers)
    elif operator == '>':
        return 1 if numbers[1] > numbers[0] else 0
    elif operator == '<':
        return 1 if numbers[1] < numbers[0] else 0
    elif operator == '=':
        return 1 if numbers[0] == numbers[1] else 0


def read_version_and_type() -> None:
    global binary_str
    global version_sum
    packet_version: int = int(binary_str[0:3], 2)
    packet_type_id: int = int(binary_str[3:6], 2)
    binary_str = binary_str[6:]

    subtract_length(6)
    version_sum += packet_version

    if packet_type_id == LITERAL_VALUE:
        formula.append(str(read_literal()))
    else:
        formula.append(convert_operator(packet_type_id))
        print("OPERATION: ", convert_operator(packet_type_id))
        read_operator()


def read_literal() -> int:
    global binary_str
    keep_reading: bool = True
    literal_length: int = 0
    literal_value_str: str = ''
    while keep_reading:
        prefix_bit: str = binary_str[0]
        literal_length += 1
        if prefix_bit == '0':
            keep_reading = False
        literal_value_str += binary_str[1:5]
        binary_str = binary_str[5:]
        literal_length += 4
    literal_value: int = int(literal_value_str, 2)
    print("LITERAL_VALUE: ", literal_value)
    subtract_length(literal_length)
    return literal_value


def read_operator() -> None:
    global binary_str
    length_type: int = int(binary_str[0])
    binary_str = binary_str[1:]
    subtract_length(1)
    if length_type == SUBPACKET_LENGTH:  # length of sub-packet
        subpacket_length: int = int(binary_str[0:15], 2)
        subtract_length(15)
        subpacket_lengths.append(subpacket_length)
        binary_str = binary_str[15:]
        while subpacket_lengths[-1] > 0:
            read_version_and_type()
        del subpacket_lengths[-1]
    elif length_type == NB_SUBPACKETS:  # number of sub-packets
        nb_subpackets: int = int(binary_str[0:11], 2)
        binary_str = binary_str[11:]
        subtract_length(11)
        while nb_subpackets > 0:
            read_version_and_type()
            nb_subpackets -= 1
    formula.append(str(perform_operation()))


read_version_and_type()

answer: int = int(formula[0])
print("ANSWER = {0}".format(answer))
