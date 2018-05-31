class Board:
	def __init__(self):
		self.cells = [None, None, None,
					  None, None, None,
					  None, None, None]

	def print_board(self):
		for i in range(len(self.cells)):
			if i % 3 == 0:
				print()
			if self.cells[i]:
				print(self.cells[i], end=" ")
			else:
				print(" |", end="")

	def check_win(self, symbol):
		"""
		Check all win combinations
		"""
		b = self.cells

		for i in range(3):
			if b[i] == symbol and b[i + 3] == symbol and \
					b[i + 6] == symbol:
				return True
			elif b[(i * 3)] == symbol and b[
				(i * 3) + 1] == symbol and b[
				(i * 3) + 2] == symbol:
				return True

			if b[0] == symbol and b[4] == symbol and \
					b[8] == symbol:
				return True
			elif b[2] == symbol and b[4] == symbol and \
					b[6] == symbol:
				return True
		return False


class Player():
	def __init__(self, symbol):
		self.symbol = symbol

	def choose_cell(self):
		"""
		Ask player to choose the cell
		"""
		options = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
		cell = input("Enter the num of cell:")
		if cell in options:
			return int(cell)
		else:
			raise Exception ("Enter the cell from 0-8")



