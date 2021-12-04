from getdayarr import getday
inp = getday(2)


x,y = 0,0

for s in inp:
    dir,val = s.split()
    val = int(val)
    if dir[0] == 'f':
        x += val
    elif dir[0] == 'd':
        y += val
    else:
        y -= val

#print(x*y)

# actual course

x,y,aim = 0,0,0

for s in inp:
    dir,val = s.split()
    val = int(val)
    if dir[0] == 'f':
        x += val
        y += val*aim
    elif dir[0] == 'd':
        aim += val
    else:
        aim -= val

print(x*y)