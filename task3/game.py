from board import *


class Game(Board):
	def __init__(self, board):
		super().__init__()
		self.player1 = Player("X")
		self.step = 0
		self.player2 = Player("0")
		self.board = board

	def start(self):
		"""
		Run all the methods
		"""
		a = False
		while a == False:
			if self.step % 2 == 0:
				cell1 = self.player1.choose_cell()
				if self.board.cells[int(cell1)] == None:
					self.board.cells[cell1] = str(self.player1.symbol)
				else:
					return "Choose the free cell "
				self.board.print_board()
				self.step += 1
				check = self.board.check_win(self.player1.symbol)
				if check == True:
					a = True
					return "Result:\n {} win".format(self.player1.symbol)

			else:
				cell2 = self.player2.choose_cell()
				if self.board.cells[int(cell2)] == None:
					self.board.cells[cell2] = str(self.player1.symbol)
				else:
					return "Choose the free cell "
				self.board.print_board()
				self.step += 1
				check = self.board.check_win(self.player2.symbol)

				if check == True:
					a = True
					return "Result:\n {} win".format(self.player2.symbol)


c = Board()
d = Game(c)
print(d.start())
