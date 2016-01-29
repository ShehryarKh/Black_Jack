class View:

	def choice(self):
		print("what would you like to do")
		print("Press 'h' for hit")
		print("Press 's' for stay")

# intro message 
	def intro(self):
		print("welcome to BlackJack!!!")
		print("google how to play if you dont know how to")
#log in
	def log_In(self):
		username = input("Enter your name : ")
		password = input("enter your password : ")
		login = { "username": username, "password": password}
		return login
# if your account doesnt exisit
	def Invalid_account(self):
		print("you sure you registerd?")

	def ruled(self):
		print("""
			Black jack is a card game played between the player and the dealer.

    At the start, both you and the dealer are dealt two cards. The dealer shows
you his first.

    Your cards, or hand, have a score. You get your score by
adding up the values of each card in your hand. Every number card's value is
its number, and any face card is worth 10. Ace is worth 1 or 11, whichever is
most beneficial for the player. The winner of the game is whoever's score is
closest to 21. Ties go to the dealer.

    With your two cards, you have the option to hit or stay. Hit means draw one
more card. Stay means you're happy with your score.
			""")
