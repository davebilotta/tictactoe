def hasWinner(board):
	#
	# Determine if board has a winner 
	# 

	winner = False
	
	#
	# Check Horizontal 
    #
	for x in range(0,3):
		if ((board[x][0] == 0) or (board[x][1] == 0) or (board[x][2] == 0)):
			# Do nothing
			1

		# Check winner (horizontal)
		elif (board[x][0] == board[x][1] == board[x][2]):
			winner = True

    # 
    # Check Vertical 
    # 

	if (not winner):
		for y in range(0,3):
			if ((board[0][y] == 0) or (board[1][y] == 0) or (board[2][y] == 0)):
				# Do nothing 
				1
			
			# Check winner (vertical)
			elif (board[0][y] == board[1][y] == board[2][y]):
				winner = True

    # 
    # Check Diagonal 
    #
	if (not winner):
		if ((board[0][0] == 0) or (board[1][1] == 0) or (board[2][2] == 0)):
			# Do nothing 
			1
		elif ((board[0][2] == 0) or (board[1][1] == 0) or (board[2][0] == 0)):
			# Do nothing 
			1

		# Check winner on the diagonal
		elif (board[0][0] == board[1][1] == board[2][2]):
			winner = True

		# Check winner on the other diagonal
		elif (board[0][2] == board[1][1] == board[2][0]):
			winner = True

	return winner

def checkWinner(board):
	# 
	# Find out who won (X or O) 
	#
	return False

def answer(board,playerX):
    # if playerX - player is X, AI is O 
    # else AI is X 

    print board