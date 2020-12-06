file = open('C:\\Users\\lmera\\OneDrive\\Desktop\\AdvenToCodePy\\Code\\input2.txt', 'r')
line = file.readline()
correct = 0

while line:
    # Set up variables
    arr = line.split(' ')
    position = arr[0].split('-')
    pos1 = int(position[0])-1
    pos2 = int(position[1])-1
    char = arr[1][:-1]
    password = arr[2].split('\n')[0]
    print(password[pos1])

    # Check if password is correct
    if password[pos1] == char and password[pos2] != char:
        correct += 1
    elif password[pos1] != char and password[pos2] == char:
        correct += 1

    line = file.readline()
file.close()

print("Number of Incorrect Passwords: " + str(correct))
