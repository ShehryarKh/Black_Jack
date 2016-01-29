from view import View
import pdb
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
		print("hey you have " + str(self.funds) + "dollars" )
		#return self.user

		
class card:
	def __init__(self,type,card):
		self.view = View()
		self.type  = type


	def cards(self,card):
		deck=[]
		value = ['1','2','3','4','5','6','7','8','9','10']
		type_number= ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
		#for i in
		#deck.append((c,i))

#class Deck


game = Game()
game.start()
game.load_funs()