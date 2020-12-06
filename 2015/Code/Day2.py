def calcSurface(l, w, h):
    area1 = l*w
    area2 = l*h
    area3 = w*h
    small = min(area1, area2, area3)
    surf = 2*area1 + 2*area2 + 2*area3 + small
    return surf

totalSurf = 0
file = open('input2.txt')
line = file.readline().split('\n')[0]
dim = line.split('x')
totalSurf += calcSurface(int(dim[0]), int(dim[1]), int(dim[2]))

while line:
    line = file.readline().split('\n')[0]
    dim = line.split('x')
    if dim[0] != '':
        totalSurf += calcSurface(int(dim[0]), int(dim[1]), int(dim[2]))
file.close()

print("Result: " + str(totalSurf))
