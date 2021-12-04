def getday(day: int):
    with open(f"inputs/day{day}.txt") as f:
        inp = f.read()
        inp = inp.split('\n')
    return inp