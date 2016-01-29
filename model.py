import sqlite3

class UserDatabase:

	def __init__(self):
		self.file_name="databasename.db"
		self.username = ''
		self.password = ''

	def view_account(self,login):
		self.username=login['username']
		self.password=login['password']
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()
		cursor.execute(
			""" SELECT * FROM Users WHERE username = ? AND password = ?; """,(self.username,self.password))

		row = cursor.fetchone()
		conn.commit()
		conn.close()
		if row == None:
			return False
		return True
	
	def load_funds(self):
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

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