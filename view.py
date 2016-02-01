import time

class View:

	def intro(self):
		print("Welcome to BlackJack!\n")
		username = input("Enter username:")
		password = input("Enter password:")
		login = {"username":username,"password":password}
		return login 

	def no_account(self):
		print("No Account Exists!")

	def menu(self,name,funds):
		choice = input("""
\n{}, your available funds are ${}.

	[1] Play BlackJack
	[2] Quit


""".format(name,funds))
		return choice 

	def ask_amount_to_bet(self):
		print("Bills accepted are $100, $50, $20, $10, $5")
		choice = input("Enter bet amount:$")

		return choice

	def incorrect_input(self):
		print("\nIncorrect input! Enter an integer!!")

	def insufficient_funds(self,funds):
		print("\nInsufficient funds!")
		print("Your balance is ${}".format(funds))
		
	def invalid_bet_amount(self):
		print(
		"""
	___ 	___

	    ____

	    Bet a valid number please!
		""")	

	def player_hit(self,a,a2):
		print("Your two cards are")
		for x in [".",".\n"]:
			time.sleep(.45)
			print(x)
		print(a + " & " + a2)

	def house_hit(self,card):
		print("House card is")
		for x in [".",".\n"]:
			time.sleep(.45)
			print(x)
		print(card)
		

	def blackjack(self):
		print("You got Blackjack!")


	def hands(self,yh,hh):
		for x in [".",".\n"]:
			time.sleep(.45)
			print(x)
		print(
"""
Your hand: 			
{}                 								
 
House hand:
{}                    

""".format(yh,hh))

			
	def hit_stay(self):
		choice = input("[h] hit [s] stay:")
		return choice

	def hit(self,card):
		for x in [".",".",".\n"]:
			time.sleep(.45)
			print(x)
		print(card)

	def you_win(self):
		print("YOU WIN !")

	def house_win(self):
		print("House wins")



	def you_lose(self):
		print("BUST!")
		print("LOSER!!!")

	def house_bust(self):
		print("The House BUST!")
		print("YOU WIN!")

	def push(self):
		print("Push")
		print("You win back your bet")