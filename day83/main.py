from board import GameBoard


print("Welcome to Tic-Tac-Toe!\n\n")
keep_playing = True

while keep_playing:
	while True:
		first_char = input("Choose a letter character for the first player:\n(If more than one character is taken, only the first will be used) ")
		second_char = input("Choose a letter character for the second player:\n(If more than one character is taken, only the first will be used) ")
		if first_char=="" or second_char=="":
			print("One of you cheeky buggers is trying to be an empty character! Stop that!")
		elif first_char[0]==" " or second_char[0]==" ":
			print("One of you cheeky buggers is trying to be the space character! Stop that!")
		elif second_char[0]==first_char[0]:
			print("Uh-oh, both of you are trying to use the same character!")
		else:
			#first_char = first_char[0]
			#second_char = second_char[0]
			break
			
	game = GameBoard()
	game.draw_board()
	print("To choose a position, use the\n  Q/W/E\n  A/S/D\n  Z/X/C\nkeys that correspond to the position you'd like in the square.")
	while True:
		while True:
			gvm1 = game.make_move(input(f"Player 1 ({first_char}), choose a spot: "), first_char[0]) # game valid move
			if gvm1:
				break
		game.draw_board()
		if game.check_for_win(first_char[0]):
			print(f"Player 1 ({first_char}) wins!")
			break
		if not game.check_poss_move():
			print("Looks like a tie!")
			break
		while True:
			gvm2 = game.make_move(input(f"Player 2 ({second_char}), choose a spot: "), second_char[0]) # game valid move
			if gvm2:
				break
		game.draw_board()
		if game.check_for_win(second_char[0]):
			print(f"Player 2 ({second_char}) wins!")
			break
		if not game.check_poss_move():
			print("Looks like a tie!")
			break
			
	print("Thank you for playing!")
	usr_kp = input("Would you like to play again? Type 'y' or 'yes', or any other key for no: ").lower()
	if (usr_kp!= "y") and (usr_kp!="yes"):
		keep_playing=False
