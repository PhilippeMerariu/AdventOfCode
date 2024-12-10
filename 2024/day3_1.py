import re

file = open('input3.txt')
line = file.readline()

result = 0
regex = '(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\))'
enabled = True

while line:
    res = re.findall(regex, line)
    for r in res:
        if r == "do()":
            enabled = True
        elif r == "don\'t()":
            enabled = False
        else:
            r = r.replace('mul(', '')[:-1]
            x, y = r.split(',')
            if enabled:
                result += int(x) * int(y)
    line = file.readline()
file.close()

print(f"ANSWER = {result}")
