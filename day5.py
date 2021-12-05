from getdayarr import getday

inp = getday(5)

lines = []

ymax,xmax = 0,0

# format the input
for line in inp:
    line = line.split(' -> ')
    line = [list(map(int,line[0].split(','))),list(map(int,line[1].split(',')))]
    for point in line:
        if point[0] > xmax:
            xmax = point[0]
        if point[1] > ymax:
            ymax = point[1]
    lines.append(line)

print(lines[0])

# create grid
grid = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]

print(xmax,ymax,'\n')

# helper functions
direction = lambda coord1,coord2: (1 if coord2 > coord1 else -1 if coord2 < coord1 else 0)
absdist = lambda coord1,coord2: abs(coord1-coord2)

for line in lines:
    #if line[0][0] == line[1][0] or line[0][1] == line[1][1]:  # only straight lines
    if True:                                                   # all lines
        diff = [direction(line[0][0], line[1][0]),direction(line[0][1], line[1][1])]  # gets the sign of the difference in both the x and y direction
        pos = line[0]  # define start position
        for i in range(max(absdist(line[0][0],line[1][0]),absdist(line[0][1],line[1][1]))+1):  # in case of a straigt line get the max of the 2 absolute differences (plus 1 since it is inclusive)
            grid[pos[1]+i*diff[1]][pos[0]+i*diff[0]] += 1
crossings = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] > 1:
            crossings += 1

print(crossings)
