
class GameBoard:
	def __init__(self):
		self.boardpos = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
	
	def draw_board(self):
		print("\n-------------")
		for each_row in self.boardpos:
			print(f"| {each_row[0]} | {each_row[1]} | {each_row[2]} |\n")
			print("-------------")
		print("\n")
		
	def find_pos(self, given_char):
		given_char = given_char.lower()
		if (given_char=='q'):
			return (0,0)
		elif (given_char=='w'):
			return (0,1)
		elif (given_char=='e'):
			return (0,2)
		elif (given_char=='a'):
			return (1,0)
		elif (given_char=='s'):
			return (1,1)
		elif (given_char=='d'):
			return (1,2)
		elif (given_char=='z'):
			return (2,0)
		elif (given_char=='x'):
			return (2,1)
		elif (given_char=='c'):
			return (2,2)
		
	
	def make_move(self, pos_char, play_char):
		spot = self.find_pos(pos_char)
		if (spot is not None) and (self.boardpos[spot[0]][spot[1]]== " "):
			self.boardpos[spot[0]][spot[1]] = play_char
			return True
		else:
			print("Invalid key pressed!")
			return False
	
	def check_poss_move(self):
		for row in self.boardpos:
			for el in row:
				if (el == " "):
					return True
		return False
	
	def check_for_win(self, player_char):
		pchar_winning = [player_char] * 3
		# check the rows
		for row in self.boardpos:
			if row == pchar_winning:
				return True
		# check columns
		for i in range(3):
			if [self.boardpos[0][i], self.boardpos[1][i], self.boardpos[2][i]] == pchar_winning:
				return True
		# check diagonals
		if [self.boardpos[0][0], self.boardpos[1][1], self.boardpos[2][2]] == pchar_winning:
				return True
		if [self.boardpos[2][0], self.boardpos[1][1], self.boardpos[0][2]] == pchar_winning:
				return True
		# otherwise no wins yet
		return False
