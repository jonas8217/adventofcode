from getdayarr import getday

inp = getday(12)

paths = [row.split('-') for row in inp]

print(paths)

start = 'start'
end = 'end'


def getconnections(cave):
    connected = []
    for path in paths:
        if cave in path:
            if path[0] == cave:
                connected.append(path[1])
            else:
                connected.append(path[0])
    return connected


def isbig(cave):
    return cave.upper() == cave




def findpath(takenpath,cave,totalpaths):
    if cave == end:
        totalpaths += 1
    for connection in getconnections(cave):
        if connection not in takenpath or isbig(connection):
            totalpaths = findpath(takenpath+[cave],connection,totalpaths)
    return totalpaths



print(findpath([],start,0))

allpaths = set()


def findpathplus1small(takenpath,cave,totalpaths,smalltwice):
    if cave == end:
        totalpaths += 1
        allpaths.add(tuple(takenpath+[end]))
        return totalpaths
    for connection in getconnections(cave):
        if (connection not in takenpath or isbig(connection) or not smalltwice) and connection != start:
            if not isbig(connection) and connection in takenpath:
                totalpaths = findpathplus1small(takenpath+[cave],connection,totalpaths,True)
            else:
                totalpaths = findpathplus1small(takenpath+[cave],connection,totalpaths,smalltwice)
    return totalpaths


print(findpathplus1small([],start,0,False))
print(len(allpaths))
print(list(allpaths)[:10])