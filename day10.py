from getdayarr import getday

inp = getday(10)

"""
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
"""
points = [3,57,1197,25137]
open = '([{<'
close = ')]}>'




score = 0

for line in inp:
    toclose = ''

    for char in line.strip():
        if char in open:
            toclose += char
        elif open.index(toclose[-1]) == close.index(char):
            toclose = toclose[:-1]
        else:
            score += points[close.index(char)]
            print('expected', toclose[-1], 'got', char)
            break


print(score)


scores = []
nonCorrupted = []


for line in inp:
    toclose = ''
    corrupt = False
    for char in line.strip():
        if char in open:
            toclose += char
        elif open.index(toclose[-1]) == close.index(char):
            toclose = toclose[:-1]
        else:
            corrupt = True
            #print('expected', toclose[-1], 'got', char)
            break

    score = 0
    if not corrupt:
        print(toclose)
        for char in toclose[::-1]:
            score *= 5
            score += open.index(char)+1
        scores.append(score)

scores = sorted(scores)

print(scores[len(scores)//2])