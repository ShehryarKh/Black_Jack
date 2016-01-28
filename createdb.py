import sqlite3 

conn = sqlite3.connect("db.db")

conn.execute(
	"""
	CREATE TABLE Users(
		id INTEGER PRIMARY KEY,
		username TEXT,
		password TEXT,
		funds INTEGER
	);
	""")

conn.execute(
	"""
	INSERT INTO Users (username,password,funds) VALUES ("Robert","123",5000);
	""")

conn.commit()
conn.close()

print("db.db created")