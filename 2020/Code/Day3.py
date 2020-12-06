file = open('C:\\Users\\lmera\\OneDrive\\Desktop\\AdvenToCodePy\\Code\\input3.txt', 'r')
line = file.readline()
lineCount = 0
charCount = 0
treeStr = line[charCount]

while line:
    if lineCount > 0:
        charCount += 3
        if charCount >= len(line):
            print(len(line))
            charCount = charCount % len(line)
        treeStr += line[charCount]
        # if line[charCount] == '#':
        #     nbTrees += 1
    line = file.readline().split('\n')[0]
    lineCount += 1

print("Number of Trees: " + str(treeStr.count('#')))

file.close()
