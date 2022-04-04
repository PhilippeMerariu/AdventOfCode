from typing import List

LITERAL_VALUE: int = 4
SUBPACKET_LENGTH: int = 0
NB_SUBPACKETS: int = 1

file = open('input16.txt')
line = file.readline().strip()

binary_str: str = str(bin(int(line, 16)))[2:]
while len(binary_str) % 4 != 0:
    binary_str = "0" + binary_str

version_sum: int = 0
subpacket_lengths: List[int] = []


def subtract_length(val: int) -> None:
    for i in range(len(subpacket_lengths)):
        subpacket_lengths[i] -= val


def read_version_and_type() -> int:
    global binary_str
    global version_sum
    packet_version: int = int(binary_str[0:3], 2)
    packet_type_id: int = int(binary_str[3:6], 2)
    binary_str = binary_str[6:]

    nb_bits: int = 6
    subtract_length(nb_bits)
    version_sum += packet_version

    if packet_type_id == LITERAL_VALUE:
        nb_bits += read_literal()
    else:
        read_operator()

    return nb_bits


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
    return literal_length


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
            subpacket_length -= read_version_and_type()
        del subpacket_lengths[-1]
    elif length_type == NB_SUBPACKETS:  # number of sub-packets
        nb_subpackets: int = int(binary_str[0:11], 2)
        binary_str = binary_str[11:]
        subtract_length(11)
        while nb_subpackets > 0:
            read_version_and_type()
            nb_subpackets -= 1


read_version_and_type()

answer: int = version_sum
print("ANSWER = {0}".format(answer))
