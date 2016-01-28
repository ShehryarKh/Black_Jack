from view import View 
from model import * 

class Game:
	def __init__(self):
		self.view = View()
		self.choice = ''
		self.funds = None 
		self.user = UserDatabase()

	def run(self):
		while self.choice not in ["quit","q","QUIT"]:
			self.start()
			self.load_funds()
		
	def start(self):
		login = self.view.intro()
		while self.user.check_account_status(login):
			break
		else:
			self.view.no_account()
			self.start()
		
	def load_funds(self):
		self.funds = self.user.load_funds()
		



game=Game()
game.run()