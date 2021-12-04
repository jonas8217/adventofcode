from getdayarr import getday
inp = getday(3)

size = len(inp[0])
indexes = [0 for _ in range(size)]


for val in inp:
    for i in range(size):
        indexes[i] += (1 if val[i] == '1' else -1)

sbin = ""
for val in indexes:
    sbin += ('1' if val > 0 else '0')

#print(indexes)
#print(int(sbin,2)*(int(size*'1',2)-int(sbin,2)))
newinp = getday(3)
for n in range(size):
    indexval = 0
    for val in newinp:
        indexval += (1 if val[n] == '1' else -1)

    if indexval == 0:
        indexval = '1'
    else:
        indexval = ('1' if indexval > 0 else '0')
    tempinp = []
    for val in newinp:
        if val[n] == indexval:
            tempinp.append(val)
    newinp = tempinp
    if len(tempinp) == 1:
        break

ox = int(newinp[0],2)

newinp = getday(3)
for n in range(size):
    indexval = 0
    for val in newinp:
        indexval += (1 if val[n] == '1' else -1)

    if indexval == 0:
        indexval = '0'
    else:
        indexval = ('1' if indexval < 0 else '0')
    tempinp = []
    for val in newinp:
        if val[n] == indexval:
            tempinp.append(val)
    newinp = tempinp
    if len(tempinp) == 1:
        break

co2 = int(newinp[0],2)

print(ox,co2,ox*co2)