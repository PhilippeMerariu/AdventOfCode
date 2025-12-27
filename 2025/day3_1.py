file = open('input3.txt')
line = file.readline()

result = 0

banks = []


while line:
    line = line.strip('\n')
    bank = []
    for l in line:
        bank.append(l)
    banks.append(bank.copy())
    line = file.readline()
file.close()

for bank in banks:
    max_jolt = 0
    for i in range(len(bank) - 1):
        if int(bank[i]) < int(str(max_jolt)[0]):
            continue
        for j in range(i + 1, len(bank)):
            jolt = bank[i] + bank[j]
            max_jolt = max(int(jolt), max_jolt)
    result += int(max_jolt)


print(f"ANSWER = {result}")
