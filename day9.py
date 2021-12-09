from getdayarr import getday

inp = getday(9)

inp = """2199943210
3987894921
9856789892
8767896789
9899965678""".split('\n')

heightmap = [[int(n) for n in row]+[9] for row in inp]
heightmap += [(len(inp[0])+2)*[9]]  # padding to circumvent negatives of wrapping in python lists


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

lowest = []

for y in range(ymax):
    for x in range(xmax):
        if islowest(x,y):
            lowest.append([x,y])


def basinSearch(x,y):
    BreadthWidthToggle = 0
    basin = []
    new = [[x,y]]
    tempnew = []
    while len(new) != 0:

        print(new)
        for coord in new:
            for i in range(coord[0]+1,xmax):
                if heightmap[coord[1]][i] not in basin and heightmap[coord[1]][i] != 9:
                    tempnew.append([i,coord[1]])
                else:
                    break
            for i in range(0,coord[0]-1)[::-1]:
                if heightmap[coord[1]][i] not in basin and heightmap[coord[1]][i] != 9:
                    tempnew.append([i,coord[1]])
                else:
                    break
        new = tempnew
        tempnew = []
        print(new)
        for n in new:
            basin.append(n)

        for coord in new:
            for i in range(coord[1]+1,ymax):
                if heightmap[i][coord[0]] not in basin and heightmap[i][coord[0]] != 9:
                    tempnew.append([coord[0],1])
                else:
                    break
            for i in range(0,coord[0]-1)[::-1]:
                if heightmap[i][coord[0]] not in basin and heightmap[i][coord[0]] != 9:
                    tempnew.append([coord[0],1])
                else:
                    break
        new = tempnew
        tempnew = []
        print(new)
        break


        for n in new:
            basin.append(n)
    return basin

print(basinSearch(*lowest[0]))