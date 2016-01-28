class View:

	def intro(self):
		print("Welcome to BlackJack!")
		username = input("Enter username:")
		password = input("Enter password:")
		login = {"username":username,"password":password}
		return login 

	def no_account(self):
		print("No Account Exists!")
		




