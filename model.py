import sqlite3 

class UserDatabase: 

	def __init__(self):
		self.file_name = "db.db"
		self.username = ''
		self.password = ''

	def check_account_status(self,login):
		self.username = login["username"]
		self.password = login["password"]

		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

		cursor.execute(
			"""
			SELECT * FROM Users WHERE username = ? AND password = ?;
			""", (self.username, self.password))

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
			"""
			SELECT funds FROM Users WHERE username = ? AND password = ?; 
			""",(self.username,self.password))

		row = cursor.fetchone()
		conn.commit()
		conn.close()
		if row == None:
			return None 
		else:
			balance = row[0]
			return balance 

	def update_funds(self,funds):
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

		cursor.execute(
			"""
			UPDATE Users SET funds = ? WHERE username = ? AND password = ?;
			""",(funds,self.username,self.password))

		conn.commit()
		conn.close()
