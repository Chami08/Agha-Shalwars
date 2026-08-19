import sqlite3


# ================================
# Connect to Database
# ================================

connection = sqlite3.connect("shop.db")

cursor = connection.cursor()


# ================================
# Products Table
# ================================

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


# ================================
# Submissions Table
# ================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


# ================================
# Save Changes
# ================================

connection.commit()


# ================================
# Check Products Table
# ================================

cursor.execute("PRAGMA table_info(products)")

columns = cursor.fetchall()

print("Products table created successfully!")

print("\nColumns in products table:")

for column in columns:

    print(column)


# ================================
# Check Submissions Table
# ================================

cursor.execute("PRAGMA table_info(submissions)")

submission_columns = cursor.fetchall()

print("\nSubmissions table created successfully!")

print("\nColumns in submissions table:")

for column in submission_columns:

    print(column)


# ================================
# Close Database
# ================================

connection.close()

print("\nDatabase setup completed successfully!")