LITERAL_VALUE: int = 4

file = open('input16_test.txt')
line = file.readline().strip()

binary_str: str = str(bin(int(line, 16)))[2:]
packet_version: int = int(binary_str[0:3], 2)
packet_type_id: int = int(binary_str[3:6], 2)
binary_str = binary_str[6:]

if packet_type_id == LITERAL_VALUE:
    keep_reading: bool = True
    literal_value_str: str = ''
    while keep_reading:
        prefix_bit: str = binary_str[0]
        if prefix_bit == '0':
            keep_reading = False
        literal_value_str += binary_str[1:5]
        binary_str = binary_str[5:]
    literal_value: int = int(literal_value_str, 2)


answer: int = 0
print("ANSWER = {0}".format(answer))
