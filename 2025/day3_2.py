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
    nb_batteries = 12
    battery = ""
    max_jolt = ""
    start_idx = 0
    for _ in range(nb_batteries):
        b_subset = bank[start_idx:len(bank) - (nb_batteries - 1):]
        max_jolt = max(b_subset)
        start_idx += b_subset.index(max_jolt) + 1
        battery += max_jolt
        nb_batteries -= 1
    result += int(battery)


print(f"ANSWER = {result}")
