from getdayarr import getday

inp = getday(7)

inp = list(map(int,inp[0].split(',')))

crabsubs = [0 for _ in range(max(inp)+1)]



for crabsubindex in inp:
    crabsubs[crabsubindex] += 1

leftIndex,rightIndex = 0,len(crabsubs)-1
fueltospendleft,fueltospendright = crabsubs[0],crabsubs[-1]

fuelspent = 0


while rightIndex != leftIndex:
    if fueltospendleft > fueltospendright:
        fuelspent += fueltospendright
        crabsubs[rightIndex-1] += crabsubs[rightIndex]
        crabsubs[rightIndex] = 0
        rightIndex -= 1
        fueltospendright += crabsubs[rightIndex]
    else:
        fuelspent += fueltospendleft
        crabsubs[leftIndex+1] += crabsubs[leftIndex]
        crabsubs[leftIndex] = 0
        leftIndex += 1
        fueltospendleft += crabsubs[leftIndex]



print(fuelspent)