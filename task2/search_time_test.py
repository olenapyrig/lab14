import time
import random
from linkedbst import LinkedBST


# Read words from words.txt file and make a list
def find_word(word):
	"""
	Return the list of words
	"""
	words = []
	with open(word, "r") as file:
		for i in file:
			words.append(i.strip())
	return words


def make_bst():
	"""
	Make BST from words from words.txt
	"""
	lst = find_word("words.txt")
	bst = LinkedBST()
	for i in set(lst):
		bst.add(i)
	return bst

def list_rand_words():
	"""
	Returns 10000 random words from words.txt file
	"""
	words = find_word("words.txt")
	lst = []
	for i in range(1000):
		lst.append(random.choice(words))
	return lst


def rand_words(rand_word):
	"""
	Returns the search time of 10,000 random words in
	an ordered alphabetical dictionary.
	"""
	start = time.time()
	words = find_word("words.txt")
	lst = []
	for i in rand_word:
		lst.append(words.index(i))
	return time.time() - start


def bst_unbalanced(rand_word):
	"""
	Returns the search time of 10,000 random
	words in the dictionary, which is represented
	as a binary search tree.
	"""
	bst = make_bst()
	start = time.time()
	lst = [bst.find(i) for i in rand_word]
	return time.time() - start


def bst_balanced(rand_word):
	"""
	Returns the search time of 10,000 random
	words in the dictionary, which is represented
	as a balanced binary search tree.
	"""
	bst = make_bst()
	bst.rebalance()
	start = time.time()
	lst = [bst.find(i) for i in rand_word]
	return time.time() - start


if __name__ == "__main__":
	print("Ordered alphabetical dictionary: ",
		  rand_words(list_rand_words()))
	print("Binary search tree: ",
		  bst_unbalanced(list_rand_words()))
	print("Balanced binary search tree: ",
		  bst_unbalanced(list_rand_words()))
