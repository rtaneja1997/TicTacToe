NOT_VALID_MOVE=0 
PLAYER_WON=1
PLAYER_LOST=2 
GOOD_MOVE=3 
TIE=4


class GameState(object): 

	def __init__(self, turn):

		self._board=[[" " for j in range(3)] for i in range(3)]
		self._current_turn=turn 

	def getBoard(self):
		return self._board 

	def switchTurn(self):
		if self._current_turn=='player':
			self._current_turn='ai' 
		else:
			self._current_turn='player'

	def occupy_tile(self, r, c):
		if self._current_turn=='player':
			self._board[r][c]='X' 
		else:
			self._board[r][c]='O' 

	def getTurn(self):
		return self._current_turn 

	def printBoard(self):
		print ("       |      |       ")
		print ("  %s    |  %s   |  %s   " %((self._board)[0][0], (self._board)[0][1], (self._board)[0][2]))
		print ("       |      |       ")
		print ("----------------------")
		print ("       |      |       ")
		print ("  %s    |  %s   |  %s   " %((self._board)[1][0], (self._board)[1][1], (self._board)[1][2]))
		print ("       |      |       ")
		print ("----------------------")
		print ("       |      |       ")
		print ("  %s    |  %s   |  %s   " %((self._board)[2][0], (self._board)[2][1], (self._board)[2][2]))
		print ("       |      |       ")

def not_coordinate(move): 
	if len(move)<5:
		return True 
	#len(move) >= 5 
	first_char=move[0] 
	last_char=move[-1] 
	if not (first_char == '(' and last_char == ')'):
		return True 
	comma_idx=move.find(',')
	if comma_idx == -1:
		return True 
	row_no= move[1:comma_idx] 

	try:
		row_no=int(row_no) 
	except ValueError:
		return True 

	col_no=move[comma_idx+1:-1] 

	try:
		col_no=int(col_no) 
	except ValueError:
		return True 

	return False 



def parse_move(move): 
	"""A move is of the form (row,col). """
	
	comma=move.find(",")
	row=int(move[1:comma])-1 
	col=int(move[comma+1:-1])-1 
	return row,col

def out_of_range(row,col):
	"""Returns True if (row,col) is a coordinate on a 3x3 board, False otherwise """
	
	return (row<0 or row>2 or col<0 or col>2) 

def isOccupied(state, row, col): 
	"""Returns true if the tile at (row,col) has a mark, False otherwise """
	
	return state.getBoard()[row][col] != " "

def invalidMove(state, row, col): 
	return out_of_range(row,col) or isOccupied(state, row, col)


def row_win(state): 
	board=state.getBoard() 
	for row in board:
		if row[0]==row[1]==row[2] and row[0] != " ":
	
			return True 
	return False 

def col_win(state): 
	curr_col=0 
	curr_row=0 
	board=state.getBoard() 
	while curr_col<3:
		column=[] 
		while curr_row<3:

			column.append(board[curr_row][curr_col]) 
			curr_row+=1 
		if column[0]==column[1]==column[2] and column[0] != " ":

			return True 
		curr_col+=1 
		curr_row=0 
	return False 

def diag_win(state):
	board=state.getBoard() 
	left_diag = (board[0][0]==board[1][1]==board[2][2] and board[0][0] != " ")
	right_diag = (board[0][2]==board[1][1]==board[2][0] and board[0][2] != " ")
	return left_diag or right_diag 
	

def winning_board(state): 

	#row, column or one of two diagonals is occupied 
	return row_win(state) or col_win(state) or diag_win(state) 

def isTie(curr_state): 
	allOccupied=True 
	board=curr_state.getBoard() 
	row,col=0,0 
	while row<3:
		while col<3:
			entry=board[row][col] 
			if entry== " ":
				allOccupied=False 
			col+=1 
		col=0 
		row+=1 

	return not winning_board(curr_state) and allOccupied 

def update(curr_state, command): 
	

	if not_coordinate(command):
		return NOT_VALID_MOVE 
	row,col=parse_move(command) 

	if invalidMove(curr_state, row,col): 
		return NOT_VALID_MOVE 

	#is a valid move
	curr_state.occupy_tile(row, col) 

	#check if a player has won 
	if winning_board(curr_state):
		if curr_state.getTurn()=='player':
			return PLAYER_WON 
		else:
			return PLAYER_LOST 
	if isTie(curr_state):
		return TIE

	curr_state.switchTurn() 
	return GOOD_MOVE 
	
