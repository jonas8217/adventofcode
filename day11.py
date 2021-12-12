from getdayarr import getday

inp = getday(11)

octogrid = [[[int(octo),0] for octo in row] for row in inp]


print('\n'.join(map(str,octogrid)))

xmax,ymax = len(octogrid[0])-1,len(octogrid)-1

totalflashes = 0


def flash(grid,x,y,currentflashes):
    currentflashes += 1
    grid[y][x][1] = 1

    fx,tx,fy,ty = max(0,x-1),min(xmax,x+1),max(0,y-1),min(ymax,y+1)
    for i in range(fx,tx+1):
        for j in range(fy,ty+1):
            grid[j][i][0] += 1
            if grid[j][i][0] > 9 and grid[j][i][1] != 1:
                grid,currentflashes = flash(grid,i,j,currentflashes)
    return grid,currentflashes


def allFlash(grid):
    allflash = True
    for row in grid:
        for octo in row:
            if octo[1] != 1:
                allflash = False
    return allflash


# part 1
for i in range(100):
    for y in range(ymax+1):
        for x in range(xmax+1):
            octogrid[y][x][0] += 1
            if octogrid[y][x][0] > 9 and octogrid[y][x][1] != 1:
                octogrid,flashes = flash(octogrid,x,y,0)
                totalflashes += flashes

    # reset flash
    for y in range(ymax+1):
        for x in range(xmax+1):
            if octogrid[y][x][1] == 1:
                octogrid[y][x] = [0,0]

print(totalflashes)


# part 2
octogrid = [[[int(octo),0] for octo in row] for row in inp]


steps = 0
while True:
    steps += 1
    for y in range(ymax+1):
        for x in range(xmax+1):
            octogrid[y][x][0] += 1
            if octogrid[y][x][0] > 9 and octogrid[y][x][1] != 1:
                octogrid,flashes = flash(octogrid,x,y,0)
                totalflashes += flashes

    if allFlash(octogrid):
        break

    # reset flash
    for y in range(ymax+1):
        for x in range(xmax+1):
            if octogrid[y][x][1] == 1:
                octogrid[y][x] = [0,0]

print(steps)