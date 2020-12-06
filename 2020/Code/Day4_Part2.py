def resetFields(fields):
    for i in fields:
        fields[i] = ''

def isValid():
    for i in fields:
        if fields[i] == '' and i != 'cid':
            return 0
        elif i == 'byr':
            if int(fields[i]) < 1920 or int(fields[i]) > 2002:
                return 0
        elif i == 'iyr':
            if int(fields[i]) < 2010 or int(fields[i]) > 2020:
                return 0
        elif i == 'eyr':
            if int(fields[i]) < 2020 or int(fields[i]) > 2030:
                return 0
        elif i == 'hgt':
            print(fields[i])
            unit = fields[i][-2:]
            if unit == 'in':
                number = int(fields[i][:-2])
                if number < 59 or number > 76:
                    return 0
            elif unit == 'cm':
                number = int(fields[i][:-2])
                if number < 150 or number > 193:
                    return 0
            else:
                return 0
        elif i == 'hcl':
            first = fields[i][0]
            colour = fields[i][1:]
            validChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            if first != '#':
                return 0
            elif len(colour) != 6:
                return 0
            else:
                for char in colour:
                    if char not in validChars:
                        return 0
        elif i == 'ecl':
            validColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if fields[i] not in validColours:
                return 0
        elif i == 'pid':
            if len(fields[i]) != 9:
                return 0
    return 1


validPassport = 0
fields = {'byr': '', 'iyr': '', 'eyr': '', 'hgt': '', 'hcl': '', 'ecl': '', 'pid': '', 'cid': ''}

file = open('input4.txt')
line = file.readline().split('\n')[0]

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
