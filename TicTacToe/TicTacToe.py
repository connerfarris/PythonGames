board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player = 'X'


def printBoard(board):
	for row in board:
		print(row[0] + ' | ' + row[1] + ' | ' + row[2])


def play(board, player):
	xCoordinate = int(input('x coordinate? '))
	yCoordinate = int(input('y coordinate? '))
	while (xCoordinate not in {0,1,2} or yCoordinate not in {0,1,2} or board[yCoordinate][xCoordinate] != '_' ):
		print('invalid move, try again')
		xCoordinate = int(input('x coordinate? '))
		yCoordinate = int(input('y coordinate? '))
	board[yCoordinate][xCoordinate] = player


def gameOn(board):
	winningLines = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
					[[0, 0], [1, 1], [2, 2]], [[2, 0], [1, 1], [0, 2]]]
	xAndO = set()
	for line in winningLines:
		for coordinate in line:
			move = board[coordinate[1]][coordinate[0]]
			xAndO.add(move)
		if len(xAndO) == 1 and '_' != xAndO.pop():
			return False
		xAndO.clear()
	return True


while (gameOn(board) == True):
	play(board, player)
	if (player == 'X'):
		player = 'O'
	else:
		player = 'X'
	print()
	printBoard(board)
	print()

if (player == 'X'):
	print('\nCongrats O!')
else:
	print('\nCongrats X!')

