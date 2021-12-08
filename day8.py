from getdayarr import getday

inp = getday(8)

onefourseveneight = 0

for pair in inp:
    numbers,display = pair.split('|')
    display = display.strip().split(' ')
    for n in display:
        if len(n) in [2,3,4,7]:
            onefourseveneight += 1

print(onefourseveneight)

for pair in inp:
    numbers,display = pair.split('|')
    numbers = numbers.strip().split(' ')
    display = display.strip().split(' ')
    one = ''
    four = ''
    seven = ''
    fives = []
    sixes = []
    for n in numbers:
        length = len(n)
        if length == 2:
            one = n
        elif length == 3:
            seven = n
        elif length == 4:
            four = n
        elif length == 5:
            fives.append(n)
        elif length == 6:
            sixes.append(n)

    for c in seven:
        if c not in one:
            a = c
    outliers = []
    for c in fives[0]:
        if c not in fives[1]:
            outliers.append(c)
    for c in fives[1]:
        if c not in fives[0]:
            outliers.append(c)
    for c in fives[2]:
        if c not in fives[0]:
            outliers.append(c)


print(onefourseveneight)