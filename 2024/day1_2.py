file = open('input1.txt')
line = file.readline()

left_list = []
right_list = []

while line:
    line.strip('\n')
    left, right = line.split('   ')
    left_list.append(int(left))
    right_list.append(int(right.strip('\n')))
    line = file.readline()
file.close()

similarity = 0
for nb in left_list:
    repeats = right_list.count(nb)
    similarity += nb * repeats

print(f"ANSWER = {similarity}")
