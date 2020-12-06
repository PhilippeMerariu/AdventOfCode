def resetFields(fields):
    for i in fields:
        fields[i] = ''

def isValid():
    for i in fields:
        if fields[i] == '' and i != 'cid':
            return 0
    return 1


validPassport = 0
fields = {'byr': '', 'iyr': '', 'eyr': '', 'hgt': '', 'hcl': '', 'ecl': '', 'pid': '', 'cid': ''}

file = open('input4.txt')
line = file.readline().split('\n')[0]
# pairs = line.split(' ')
# for elem in pairs:
#     key = elem.split(':')[0]
#     value = elem.split(':')[1]
#     fields[key] = value

while line:
    if line == '\n':
        validPassport += isValid()
        resetFields(fields)
    else:
        line = line.split('\n')[0]
        pairs = line.split(' ')
        for elem in pairs:
            key = elem.split(':')[0]
            value = elem.split(':')[1]
            fields[key] = value

    line = file.readline()
file.close()

print("# of Valid Passports: " + str(validPassport))
