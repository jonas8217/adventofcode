from getdayarr import getday

increases = 0
inp = getday(1)
#inp = list(map(int,inp))

print(type(inp[0]))

for i in range(1,len(inp)):
    if inp[i] > inp[i-1]:
        increases += 1


print(increases)  # ???


# with sums of 3, (spacing of 3)
increases = 0
for i in range(3,len(inp)):
    if inp[i] > inp[i-3]:
        increases += 1

print(increases)
