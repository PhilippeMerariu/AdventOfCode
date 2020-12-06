file = open('input1.txt')
line = file.readline()
res = line.count('(') - line.count(')')
print("result: " + str(res))
file.close
