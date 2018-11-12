import random 
import game 
import ai 

welcome_message = "Greetings! This is a Tic-Tac-Toe game coded using Python."
instructions= "To select a tile, input command <(row,col)>" 


def run_game(): 
	print (welcome_message) 
	print ("") 
	print (instructions)
	choice=input("Pick H or T\n")
	while choice.upper() not in ['H', 'T']:
		 choice=input("Invalid input. Please pick H or T\n")

	#flip a coin 
	i=random.randint(0,1) 
	winner='HT'[i] 
	if winner==choice:
		turn='player'
		print ("Congratulations! You go first :)")
	else:
		turn='ai' 
		print ("Sorry, you go second :(")
	
	#game starts 
	game_ongoing=True 
	game_state = game.GameState(turn) #create a new game 

	while game_ongoing:


		if game_state.getTurn()=='ai': #AI's Turn 
			ai_status=ai.play(game_state)
			if ai_status==game.PLAYER_LOST: 
				print ("AI WON!")
				game_ongoing=False 
			if ai_status==game.TIE:
				game_ongoing=False
				print ("TIE!") 

		else: #Player Turn  
			game_state.printBoard() #display board for player 

			move=input("Please pick a tile\n") 
			status=game.update(game_state, move) 

			while status==game.NOT_VALID_MOVE: 
				move=input("Invalid tile. Please pick a tile that isn't occupied\n") 
				status=game.update(game_state, move) 

			#picked a valid tile, game updated accordingly 
			if status==game.PLAYER_WON:
				print ("CONGRATS! YOU WON!")
				game_ongoing=False 

			if status==game.TIE:
				game_ongong=False 
				print ("TIE!")

			
	game_state.printBoard() #display board for player 
	

if __name__ == "__main__":
	run_game() #runs the entire game 

	#once game finished, prompt player to play agan or quit 
	restart= input("Thanks for playing my game! Enter YES to play again, NO to quit.\n")

	while restart not in ['YES', 'NO']: 
		restart=input("Enter NO to quit the game, YES to play again :)\n")

	if restart=="YES": 
		run_game() 

	print ("THANKS FOR PLAYING - ssj4rit")
