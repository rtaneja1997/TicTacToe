import game
import random 

def tuple_string(move): 
	row=move[0]
	col=move[1]
	return '('+str(row)+','+str(col)+')' 



def play(state): 
	"""Very crude, random algorithm where it just takes a random unoccupied slot"""
	board = state.getBoard() 
	unoccupied_slots=[] 
	row,col=0,0 
	while row<3:
		while col<3: 
			if board[row][col] == " ":
				unoccupied_slots.append((row+1,col+1))
			col+=1 
		col=0 
		row+=1 

	
	idx = random.randint(0,len(unoccupied_slots)-1)
	return game.update(state, tuple_string(unoccupied_slots[idx])) 


