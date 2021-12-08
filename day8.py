from getdayarr import getday

inp = getday(8)

onefourseveneight = 0

for pair in inp:
    inputnumbers,display = pair.split('|')
    display = display.strip().split(' ')
    for n in display:
        if len(n) in [2,3,4,7]:
            onefourseveneight += 1

print(onefourseveneight)


#  0aaa 
#1b    2c
# b     c
# b     c
#  3ddd
#4e    5f
# e     f
# e     f
#  6ggg

def disp(smap):
    print(f'  {smap[0]}  ')
    print(f'{smap[1]}    {smap[2]}')
    print(f'  {smap[3]}  ')
    print(f'{smap[4]}    {smap[5]}')
    print(f'  {smap[6]}  ')
    print('')

possible = 'abcdefg'

sum = 0

for pair in inp:
    inputnumbers,display = pair.split('|')
    inputnumbers = list(map(sorted,inputnumbers.strip().split(' ')))
    display = list(map(sorted,display.strip().split(' ')))

    segmap = ['' for _ in range(7)]
    nums = ['' for _ in range(10)]
    fives = []
    sixes = []
    for n in inputnumbers:
        length = len(n)
        if length == 2: # one
            nums[1] = n
        elif length == 3: # seven
            nums[7] = n
        elif length == 4: # four
            nums[4] = n
        elif length == 5:
            fives.append(n)
        elif length == 6:
            sixes.append(n)
        elif length == 7: # eight
            nums[8] = n

    for char in nums[7]:
        if char not in nums[1]:
            segmap[0] = char

    #   aaa 
    # x     x
    # x     x
    # X     x
    #   xxx
    # x     x
    # x     x
    # x     X
    #   xxx
    outliers = []
    for char in possible:
        if char not in sixes[0]:
            outliers.append(char)
        elif char not in sixes[1]:
            outliers.append(char)
        elif char not in sixes[2]:
            outliers.append(char)

    
    # 0 6 9
    for char in outliers:
        if char in nums[1]:
            segmap[2] = char
        elif char in nums[4]:
            segmap[3] = char
        else:
            segmap[4] = char
    
    #   aaa 
    # x     c
    # x     c
    # X     c
    #   ddd
    # e     x
    # e     x
    # e     x
    #   xxx

    if segmap[2] == nums[1][0]:
        segmap[5] = nums[1][1]
    else:
        segmap[5] = nums[1][0]
    
    #   aaa 
    # x     c
    # x     c
    # X     c
    #   ddd
    # e     f
    # e     f
    # e     f
    #   xxx


    for char in nums[4]:
        if char not in segmap:
            segmap[1] = char

    #   aaa 
    # b     c
    # b     c
    # b     c
    #   ddd
    # e     f
    # e     f
    # e     f
    #   xxx
    
    for char in possible:
        if char not in segmap:
            segmap[6] = char

    for n in fives:
        if segmap[1] not in n and segmap[5] not in n:
            nums[2] = n
        elif segmap[1] not in n and segmap[4] not in n:
            nums[3] = n
        else:
            nums[5] = n

    for n in sixes:
        if segmap[3] not in n:
            nums[0] = n
        elif segmap[2] not in n:
            nums[6] = n
        elif segmap[4] not in n:
            nums[9] = n



    displaynumber = 0
    for i,d in enumerate(display[::-1]):
        displaynumber = nums.index(d) * 10**i
    
    sum += displaynumber

print(sum)