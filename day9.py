from getdayarr import getday

inp = getday(9)



heightmap = [[int(n) for n in row.strip()]+[9] for row in inp]
heightmap += [(len(inp[0])+2)*[9]]  # padding to circumvent negatives of wrapping in python lists


xmax,ymax = len(heightmap[0])-1,len(heightmap)-1  # -1 from padding



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

lowest = []

for y in range(ymax):
    for x in range(xmax):
        if islowest(x,y):
            lowest.append([x,y])


def basinSearch(x,y):

    okX = lambda i: (heightmap[coord[1]][i] not in basin and heightmap[coord[1]][i] != 9)
    okY = lambda i: (heightmap[i][coord[0]] not in basin and heightmap[i][coord[0]] != 9)

    basin = {(x,y)}
    new = {(x,y)}
    lastSize = 0
    while len(basin) - lastSize != 0:
        lastSize = len(basin)
        tempnew = set()
        for coord in new:
            for i in range(coord[0]+1,xmax):
                if okX(i):
                    tempnew.add((i,coord[1]))
                else:
                    break
            for i in range(0,coord[0])[::-1]:
                if okX(i):
                    tempnew.add((i,coord[1]))
                else:
                    break
        for n in tempnew:
            new.add(n)
        for n in new:
            basin.add(n)
        tempnew = set()
        for coord in new:
            for i in range(coord[1]+1,ymax):
                if okY(i):
                    tempnew.add((coord[0],i))
                else:
                    break
            for i in range(0,coord[1])[::-1]:
                if okY(i):
                    tempnew.add((coord[0],i))
                else:
                    break
        new = tempnew

        for n in new:
            basin.add(n)
    return basin


basins = []

for point in lowest:
    basins.append(basinSearch(*point))

basins = sorted(basins,key=lambda x:len(x),reverse=True)

print(len(basins[0])*len(basins[1])*len(basins[2]))
