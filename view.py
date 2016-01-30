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
	[2] Transfer funds
	[3] Quit


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

	def dealer_hit(self, face):
		print("House card is")
		for x in [".",".",".\n"]:
			time.sleep(.45)
			print(x)
		print(face)
		

	
		





