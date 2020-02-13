def printBoard(board):
	for row in board:
		print(row[0] + ' | ' + row[1] + ' | ' + row[2])


def play(board, player):
	tileMap = {1: [0,0], 2: [1, 0], 3: [2, 0], 4: [0, 1], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
	tile = int(input('which tile will you play on? '))
	while (tile not in {1,2,3,4,5,6,7,8,9}):
		print('invalid move, try again')
		tile = int(input('which tile will you play on? '))
	board[tileMap[tile][1]][tileMap[tile][0]] = player


def draw(board):
	for row in board:
		if (row.count('_') > 0):
			return False
	return True


def gameOn(board):
	if (draw(board)):
		return False
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


def continuousGame():
	board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
	player = 'X'
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


continuousGame()
