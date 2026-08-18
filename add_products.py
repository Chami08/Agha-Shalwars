import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.cursor()

products = [

    # Casual Wear
    (
        "Elegant Casual Shalwar",
        "Casual Wear",
        5500,
        "Comfortable and stylish shalwar perfect for everyday wear.",
        "images/casual/casual-1.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Printed Casual Shalwar",
        "Casual Wear",
        6500,
        "A beautiful modern design suitable for casual occasions.",
        "images/casual/casual-2.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Printed Casual Shalwar",
        "Casual Wear",
        6500,
        "A beautiful modern design suitable for casual occasions.",
        "images/casual/casual-3.jpeg",
        "S,M,L,XL",
        1
    ),


    # Wedding Wear
    (
        "Embroidered Wedding Shalwar",
        "Wedding Wear",
        12500,
        "Elegant embroidery designed for weddings and special occasions.",
        "images/wedding/wedding-1.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Premium Wedding Shalwar",
        "Wedding Wear",
        15500,
        "A premium traditional design for your special moments.",
        "images/wedding/wedding-2.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Premium Wedding Shalwar",
        "Wedding Wear",
        15500,
        "A premium traditional design for your special moments.",
        "images/wedding/wedding-3.jpeg",
        "S,M,L,XL",
        1
    ),


    # Wedding Kids Wear
    (
        "Wedding Kids Dress",
        "Wedding Kids Wear",
        12500,
        "Elegant embroidery designed for weddings and special occasions.",
        "images/weddingkids/weddingkids1.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Premium Wedding Kids Shalwar",
        "Wedding Kids Wear",
        15500,
        "A premium traditional design for your special moments.",
        "images/weddingkids/weddingkids2.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Premium Wedding Kids Shalwar",
        "Wedding Kids Wear",
        15500,
        "A premium traditional design for your special moments.",
        "images/weddingkids/weddingkids3.jpeg",
        "S,M,L,XL",
        1
    ),


    # Abayas
    (
        "Classic Black Abaya",
        "Abayas",
        7500,
        "A simple and elegant abaya suitable for everyday use.",
        "images/abaya/abaya-1.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Embroidered Abaya",
        "Abayas",
        9500,
        "Elegant embroidery combined with a modern design.",
        "images/abaya/abaya-2.jpeg",
        "S,M,L,XL",
        1
    ),

    (
        "Embroidered Abaya",
        "Abayas",
        9500,
        "Elegant embroidery combined with a modern design.",
        "images/abaya/abaya-3.jpeg",
        "S,M,L,XL",
        1
    )

]


cursor.executemany("""
    INSERT INTO products
    (name, category, price, description, image, sizes, stock)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", products)


connection.commit()

print("Products added successfully!")

cursor.execute("SELECT * FROM products")

all_products = cursor.fetchall()

print("\nProducts in database:")

for product in all_products:
    print(product)


connection.close()