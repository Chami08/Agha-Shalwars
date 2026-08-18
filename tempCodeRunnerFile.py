import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    image TEXT NOT NULL,
    sizes TEXT,
    stock INTEGER DEFAULT 1
)
""")

connection.commit()

# Check the table
cursor.execute("PRAGMA table_info(products)")

columns = cursor.fetchall()

print("Products table created successfully!")
print("\nColumns in products table:")

for column in columns:
    print(column)

connection.close()