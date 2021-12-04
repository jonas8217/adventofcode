from getdayarr import getday

inp = getday(4)

numbers = map(int,inp[0].split(','))

boards = [[[],0]]

inp = inp[1:]
for i in range(len(inp)//6):
    for rownum in range(5):
        row = map(int,inp[1+i*6+rownum].strip().replace('  ',' ').split(' '))
        row = [[val,0] for val in row]

        boards[i][0].append(row)
    boards.append([[],0])
boards = boards[:-1]


def calcScore(num,board):
    sum = 0
    for row in board:
        for val in row:
            if val[1] == 0:
                sum += val[0]
    print(sum*num)


for num in numbers:
    for board in boards:
        if board[1] != 1:
            for row in board[0]:
                for val in row:
                    if val[0] == num:
                        val[1] = 1
                if all([1 == val[1] for val in row]):
                    board[1] = 1
                    calcScore(num,board[0])
            for colnum in range(5):
                if all([1 == row[colnum][1] for row in board[0]]):
                    board[1] = 1
                    calcScore(num,board[0])


print('\n'.join(map(str,boards[99][0])))