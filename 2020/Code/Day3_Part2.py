def countTrees(right, down):
    file = open('C:\\Users\\lmera\\OneDrive\\Desktop\\AdvenToCodePy\\Code\\input3.txt', 'r')
    line = file.readline()
    lineCount = 0
    charCount = 0
    treeStr = line[charCount]
    skip = False

    while line:
        if lineCount > 0 and not(skip):
            charCount += right
            if charCount >= len(line):
                print(len(line))
                charCount = charCount % len(line)
            treeStr += line[charCount]
        line = file.readline().split('\n')[0]
        lineCount += 1
        if down == 2:
            skip = not(skip)
    file.close()
    return treeStr.count("#")


tree11 = countTrees(1, 1)
tree31 = countTrees(3, 1)
tree51 = countTrees(5, 1)
tree71 = countTrees(7, 1)
tree12 = countTrees(1, 2)
res = tree11 * tree31 * tree51 * tree71 * tree12
print("Result: " + str(res))
