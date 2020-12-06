def calcVolume(l, w, h):
    return l*w*h

def calcDist(dim):
    dim = [int(i) for i in dim]
    dim = sorted(dim)
    return 2*int(dim[0]) + 2*int(dim[1])

totalDist = 0
file = open('input2.txt')
line = file.readline().split('\n')[0]
dim = line.split('x')
totalDist += calcDist(dim)
totalDist += calcVolume(int(dim[0]), int(dim[1]), int(dim[2]))

while line:
    line = file.readline().split('\n')[0]
    dim = line.split('x')
    if dim[0] != '':
        totalDist += calcDist(dim)
        totalDist += calcVolume(int(dim[0]), int(dim[1]), int(dim[2]))
file.close()

print("Result: " + str(totalDist))
