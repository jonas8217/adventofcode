from getdayarr import getday
from copy import copy

inp = getday(14)


polymer = inp[0]

pairs = inp[2:]

# part 1

for step in range(2):
    j = 0
    for i in range(len(polymer)-1):
        for pair in pairs:
            inpair,elem = pair.split(' -> ')
            if polymer[i+j:i+j+2] == inpair:
                j += 1
                polymer = polymer[:i+j]+elem+polymer[i+j:]
                break

counts = []
for elem in set(list(polymer)):
    counts.append((polymer.count(elem),elem))

counts = sorted(counts,reverse=True)

print(int(counts[0][0])-int(counts[-1][0]))
print()


# part 2

polymer = inp[0]
pairs = inp[2:]

polymerpatterns = dict([[pair.split(' -> ')[0],0] for pair in pairs])

pairs = dict([pair.split(' -> ') for pair in pairs])

for i in range(len(polymer)-1):
    polymerpatterns[polymer[i:i+2]] += 1

temppolymerpatterns = copy(polymerpatterns)

elements = set()

for pair,elem in pairs:
    elements.add(elem) 

counts = []
for i,elem in enumerate(elements):
    counts.append([elem,polymer.count(elem)])

counts = dict(counts)

for step in range(40):
    for patt in polymerpatterns:
        newelem = pairs[patt]
        patterncount = polymerpatterns[patt]
        counts[newelem] += patterncount
        temppolymerpatterns[patt[0]+newelem] += patterncount
        temppolymerpatterns[newelem+patt[1]] += patterncount
        temppolymerpatterns[patt] -= patterncount
    polymerpatterns = copy(temppolymerpatterns)

print(max(counts.values())-min(counts.values()))