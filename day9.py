from getdayarr import getday

inp = getday(9)


heightmap = [[int(n) for n in row]+[9] for row in inp]
heightmap += [(len(inp[0])+2)*[9]]  # padding to circumvent negatives of wrapping in python lists

print(heightmap)

xmax,ymax = len(inp[0]),len(inp)



def islowest(x,y):
    return (heightmap[y][x-1] > heightmap[y][x] < heightmap[y][x+1]) and (heightmap[y-1][x] > heightmap[y][x] < heightmap[y+1][x])


# part 1
risklevel = 0

for y in range(ymax):
    for x in range(xmax):
        if islowest(x,y):
            risklevel += heightmap[y][x] + 1

print(risklevel)


# part 2

basins = []

for y in range(ymax):
    for x in range(xmax):
        if islowest(x,y):
            basins.append([x,y])


def basinSearch(x,y):
    BreadthWidthToggle = 0
    basin = []
    new = [[x,y]]
    while len(new) != 0:
        tempnew = []

        if BreadthWidthToggle % 2 == 0:
            for coord in new:
                for i in range(coord[0]+1,xmax):
                    if heightmap[coord[1]][i] in basin:
                        break
                    elif heightmap[coord[1]][i] != 9:
                        tempnew.append([i,coord[1]])
                    else:
                        break
                for i in range(0,coord[0]-1)[::-1]:
                    if heightmap[coord[1]][i] in basin:
                        break
                    elif heightmap[coord[1]][i] != 9:
                        tempnew.append([i,coord[1]])
                    else:
                        break
            new = tempnew
        else:
            for coord in new:
                for i in range(coord[1]+1,ymax):
                    if heightmap[coord[1]][coord[0]] in basin:
                        break
                    elif heightmap[coord[1]][coord[0]] != 9:
                        tempnew.append([i,coord[0]])
                    else:
                        break
                for i in range(0,coord[0]-1)[::-1]:
                    if heightmap[coord[1]][coord[0]] in basin:
                        break
                    elif heightmap[coord[1]][coord[0]] != 9:
                        tempnew.append([i,coord[0]])
                    else:
                        break
            new = tempnew


        for n in new:
            basin.append(n)