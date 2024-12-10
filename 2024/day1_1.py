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

left_list = sorted(left_list)
right_list = sorted(right_list)

total_distance = 0
for i in range(len(left_list)):
    dist = abs(left_list[i] - right_list[i])
    total_distance += dist

print(f"ANSWER = {total_distance}")
