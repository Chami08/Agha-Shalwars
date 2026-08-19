import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

#this is for creating the admins table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL
)
""")
#this is for creating the default admin account
username = "admin"
password = "admin123"

#this is used for hash the password 
hashed_password = generate_password_hash(password)

# thsi is for add the admin account
try:
	cursor.execute(
		"INSERT INTO admins (username, password) VALUES (?, ?)",
		(username, hashed_password),
	)
	print("Admin account created successfully!")
	
except sqlite3.IntegrityError:
	print("Admin account already exists.")

connection.commit()
connection.close()

print("Admin database setup completed.")