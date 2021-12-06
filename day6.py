from getdayarr import getday

inp = getday(6)
fishlist = list(map(int,inp[0].split(',')))

fishbunch = [0 for _ in range(9)]
for fish in fishlist:
    fishbunch[fish] += 1

print(fishbunch)

for day in range(256):
    toadd = fishbunch[0]
    front = fishbunch.pop(0)
    fishbunch[6] += front
    fishbunch.append(toadd)

    print(fishbunch)
    print("day:",day+1)

print(sum(fishbunch))