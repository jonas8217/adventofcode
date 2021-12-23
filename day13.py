from getdayarr import getday

inp = getday(13)

folds = inp[-12:]
dots = inp[:-13]

grid = [[0 for _ in range(int(folds[0][-3:])*2+1)] for _ in range(int(folds[1][-3:])*2+1)]


for dot in dots:
    x,y = map(int,dot.split(','))
    grid[y][x] += 1

# part 1

d,coord = folds[0][len('fold along '):].split('=')
coord = int(coord)

for y in range(len(grid)):
    for x in range(coord):
        grid[y][x] += grid[y][-x-1]
for y in range(len(grid)):
    grid[y] = grid[y][:coord]


visible = 0

for row in grid:
    for dot in row:
        if dot > 0:
            visible += 1

print(visible)


# part 2

for fold in folds:
    d,coord = fold[len('fold along '):].split('=')
    coord = int(coord)

    if d == 'x':
        for y in range(len(grid)):
            for x in range(coord):
                grid[y][x] += grid[y][-x-1]
        for y in range(len(grid)):
            grid[y] = grid[y][:coord]
    else:
        for y in range(coord):
            for x in range(len(grid[0])):
                grid[y][x] += grid[-y-1][x]
        grid = grid[:coord]

isvisible = lambda l: ['#' if i > 0 else ' ' for i in l]

def prnt(g):
    for l in g:
        print(''.join(isvisible(l)))

prnt(grid)