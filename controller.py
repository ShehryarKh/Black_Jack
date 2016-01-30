
from view import View 
from model import * 
import time
import random

class Game:
	

	def __init__(self):
		self.view = View()
		self.choice = ''
		self.deck = Deck()
		self.funds = None 
		self.table = None
		self.username = ''
		self.user = UserDatabase()
		self.quit = ["quit","q","QUIT"]
		self.over = False

	
		

	def run(self):
		while self.choice not in self.quit:
			self.start()
			self.load_funds()
			self.menu()
			self.play()
							
	def start(self):
		login = self.view.intro()
		self.username = login["username"]

		while self.user.check_account_status(login):
			break
		else:
			self.view.no_account()
			self.start()
		
	def load_funds(self):
		self.funds = self.user.load_funds()

	def menu(self):
		self.choice = self.view.menu(name = self.username,funds = self.funds)
		if self.choice == "1":
			while self.ask_amount_to_bet():
				break 
		elif self.choice == "2":
			self.transfer()
		elif self.choice == "3":
			self.choice = "quit"
		else:
			self.menu()
		
	def ask_amount_to_bet(self):
		self.choice = self.view.ask_amount_to_bet()
		while self.choice not in self.quit:
			break 
		if self.choice.isdigit():
			self.choice = int(self.choice)
			if self.funds >= self.choice and self.choice >1:
				if self.choice % 100 == 0 or self.choice % 50 == 0 or self.choice % 20 == 0 or self.choice % 10 == 0 or self.choice % 5 == 0:
					self.funds -= self.choice
					self.table = self.choice
					return True 
				elif self.funds < self.choice:
						self.view.insufficient_funds(funds = self.funds)
						time.sleep(.5)
						self.menu()
				else:
					self.view.invalid_bet_amount()
					self.menu()
		else:
			self.view.incorrect_input()
			self.menu()

	def play(self):
		c = self.deck.hit()
		self.view.dealer_hit(c["face"])
		self.choice = "quit"

			

		
class Deck:
	def __init__(self):
		self.cards = []
		suit = [" H", " S", " D"," C"]
		card = ["2","3","3","4","5","6","7","8","9","10","J","Q","K","A"]

		for c in card:
			if not c.isdigit():
				value = 10
			else:
				value = int(c)
			ace = False if c != "A" else True 
			for s in suit:
				a_card = {"face":c+s,"value": value,"ace":ace}
				self.cards.append(a_card)
		random.shuffle(self.cards)

	def hit(self):
		return self.cards.pop()


		
		

			




		




game=Game()
game.run()














