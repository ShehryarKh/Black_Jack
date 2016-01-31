import sqlite3
# my model class which loads and saves things to the databse
class UserDatabase:
# init metion which creates the database file
# initlized usernam and password for later use
	def __init__(self):
		self.file_name="databasename.db"
		# these is empty because its usere input
		self.username = ''
		self.password = ''
# function whih checks if your account exists or not
	def view_account(self,login):
		# login method is called in view.py
		self.username=login['username']
		self.password=login['password']
		# connecting to database
		conn = sqlite3.connect(self.file_name)
		# set up cursor object which calls the exicute
		cursor = conn.cursor()
		# use of self.username and self.password
		cursor.execute(
			""" SELECT * FROM Users WHERE username = ? AND password = ?; """,(self.username,self.password))
		# fetchone() selects the first row
		row = cursor.fetchone()
		# commit the changes and 
		conn.commit()
		conn.close()
		#if the first row doesnt not exist return false 
		if row == None:
			return False
		# else return true
		return True
	# function to load funds
	def load_funds(self):
		# create connection to database
		conn = sqlite3.connect(self.file_name)
		# cursor object to call the execute
		cursor = conn.cursor()
		# call the execute function
		cursor.execute(
			""" SELECT funds FROM Users WHERE username = ? AND password = ?;""",(self.username, self.password))

		row = cursor.fetchone()
		conn.commit()
		conn.close()
		if row == None:
			return None
		else:
			funds = row[0]
			return funds