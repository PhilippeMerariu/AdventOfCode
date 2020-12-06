file = open('C:\\Users\\lmera\\OneDrive\\Desktop\\AdvenToCodePy\\Code\\input2.txt', 'r')
line = file.readline()
correct = 0
count = 0

while line:
    # Set up variables
    arr = line.split(' ')
    minmax = arr[0].split('-')
    min = minmax[0]
    max = minmax[1]
    char = arr[1][:-1]
    password = arr[2].split('\n')[0]
    charCount = password.count(char)
    count = count + 1
    # Check if password is correct
    if int(min) <= charCount <= int(max):
        correct += 1

    line = file.readline()
file.close()

print("Number of Incorrect Passwords: " + str(correct))
