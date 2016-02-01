
from view import View 
from model import * 
import time
import random

class Game:
	def __init__(self):
		self.view = View()
		self.choice = ''
		self.deck = Deck()
		self.funds = 0 
		self.table = 0
		self.username = ''
		self.user = UserDatabase()
		self.quit = ["quit","q","QUIT"]
		self.over = False
		self.yh = '' 
		self.yh_value = 0
		self.hh = ''
		self.hh_value = 0
		self.bet = 0
		
	def run(self):
		while self.choice not in self.quit:
			self.start()
			self.menu()		
							
	def start(self):
		login = self.view.intro()

		if self.user.check_account_status(login):
			self.username = login["username"]
			self.load_funds()
			
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
			self.play() 
		elif self.choice == "2":
			self.choice = "quit"
			pass 
		else:
			self.menu()
		
	def ask_amount_to_bet(self):
		self.choice = self.view.ask_amount_to_bet()
		while self.choice not in self.quit:
			break 
		if self.choice.isdigit():
			self.bet = int(self.choice)
			if self.funds >= self.bet and self.bet >1 and self.bet <=500:
				if self.bet % 100 == 0 or self.bet % 50 == 0 or self.bet % 20 == 0 or self.bet % 10 == 0 or self.bet % 5 == 0:
					self.funds -= self.bet
					#self.table = self.bet
					return True 
			elif self.funds < self.bet:
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
		a = self.deck.hit()
		a2 = self.deck.hit()
		h = self.deck.hit()
		self.yh_value = [a["value"],a2["value"]]
		self.yh = [a["face"],a2["face"]]
		self.hh_value = [h["value"]]
		self.hh = [h["face"]]
		self.view.player_hit(a["face"],a2["face"])
		self.view.house_hit(h["face"])
		self.view.hands(self.yh,self.hh)
		self.hit()

	def hit(self):
		self.choice = self.view.hit_stay()
		while self.choice.lower() not in ["h","s"]:
			self.choice = self.view.hit_stay()
		if self.choice == "h":
			x = self.deck.hit()
			self.yh_value.append(x["value"])
			self.yh.append(x["face"])
			self.view.hands(self.yh,self.hh)
			if self.check():
				self.hit()
			else:
				self.you_bust()
		elif self.choice == "s":
			self.stay()

	def stay(self):	
		while sum(self.hh_value) < 17:
			y = self.deck.hit()
			self.hh_value.append(y["value"])
			self.hh.append(y["face"])
			self.view.hands(self.yh,self.hh)
			while self.h_check():
				break
			self.stay()

	def h_check(self):
		player_total = sum(self.yh_value)
		house_total = sum(self.hh_value)

		if house_total > 21:
			self.house_bust()
		elif house_total >=17 and house_total < player_total:
			self.player_win()
		elif house_total >= 17 and house_total > player_total:
			self.house_win()
		elif house_total == player_total and house_total >= 17:
			self.push()
		elif house_total < 17:
			return True 

	def player_win(self):
		self.view.you_win()
		win = self.bet*2
		self.funds += win 
		self.update()
		self.menu()

	def house_win(self):
		self.view.house_win()
		self.update()
		self.menu()

	def push(self):
		self.view.push()
		self.funds += self.bet 
		self.update()
		self.menu()

	def house_bust(self):
		self.view.house_bust()
		win = self.bet*2
		self.funds += win 
		self.update()
		self.menu()
		
	def check(self):
		if sum(self.yh_value) > 21:
			return False
		else:
			return True 

	def update(self):
		self.user.update_funds(funds=self.funds)

	def you_bust(self):
		self.view.you_lose()
		self.update()
		self.menu()
		
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














