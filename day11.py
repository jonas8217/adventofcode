from getdayarr import getday

inp = getday(11)

octogrid = [[[int(octo),0] for octo in row] for row in inp]

octogrid = [
    [[2,0],[8,0],[7,0]],
    [[6,0],[1,0],[7,0]],
    [[5,0],[1,0],[2,0]]
]

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
            if grid[j][i][0] >= 9 and grid[j][i][1] != 1:
                grid,currentflashes = flash(grid,i,j,currentflashes)
    return grid,currentflashes


#g,f = flash(octogrid,1,1,0)
#rint('\n'.join(map(str,g)))

for i in range(5):
    for y in range(ymax+1):
        for x in range(xmax+1):
            octogrid[y][x][0] += 1
            if octogrid[y][x][0] >= 9 and octogrid[y][x][1] != 1:
                octogrid,flashes = flash(octogrid,x,y,0)
                totalflashes += flashes

    print('\n'.join(map(str,octogrid)))

    # reset flash
    for y in range(ymax+1):
        for x in range(xmax+1):
            if octogrid[y][x][1] == 1:
                octogrid[y][x] = [0,0]
    print()
    print('\n'.join(map(str,octogrid)))

print(totalflashes)
