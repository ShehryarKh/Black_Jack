from view import View
import pdb
from random import shuffle
from model import *

class Game:
	def __init__ (self):
		self.view=View()
		self.choice = ''
		self.funds = None
		self.user = UserDatabase()

	def start(self):
		# calls intro function from view
		intro = self.view.intro()
		# calls Log_In function from views
		login =self.view.log_In()
		# you were able to login
		while self.user.view_account(login):
			break
		else:
			self.view.Invalid_account()
			self.start()

	def load_funs(self):
		self.funds = self.user.load_funds()
		print("Welcome you have " + str(self.funds) +" "+ "dollars" )
		#return self.user

		
class Deck:
	def __init__(self):
		self.view = View()
		self.deck = []
		self.create_deck()

	def create_deck(self):

		# type of cards
		type_card= ['C','D','H', 'S']
		# each cards value
		value = ['A','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
		# for loop that creats a list of tuples ('C','A') ,('C','2'), ('C','3') ... 
		for i in type_card :
			for v in value :
				self.deck.append((i,v))
		# shuffle the deck (from random import shuffel on top of file)
		shuffle(self.deck)

	def pop(self):
		return self.deck.pop()

	def __str__(self):
		return str(self.deck)

class Dealer:
	def __init__(self):
		self.hand = []
		self.deck = Deck()
		

	def give_1(self):
		print(self.deck)
		x = self.deck.pop()
		print(x)

	def give_2(self):
		print (self.deck)
		x = self.deck.pop()
		self.hand.append(x)
		y = self.deck.pop()
		self.hand.append(y)
		print (self.hand)
		print(self.deck)



game = Game()
game.start()
game.load_funs()
cards = Deck()
cards.create_deck()
dealer = Dealer()
dealer.give_1()
dealer.give_2()