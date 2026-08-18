from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("shop.db")
    connection.row_factory = sqlite3.Row
    return connection


# ================================
# Product Details
# ================================

@app.route("/product/<int:product_id>")
def product_details(product_id):

    connection = get_db_connection()

    product = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    connection.close()

    if product is None:
        return "Product not found", 404

    return render_template(
        "product_details.html",
        product=product
    )


# ================================
# Home
# ================================

@app.route("/")
def home():
    return render_template("index.html")


# ================================
# About
# ================================

@app.route("/about")
def about():
    return render_template("about.html")


# ================================
# Shop
# ================================

@app.route("/shop")
def shop():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products"
    ).fetchall()

    connection.close()

    return render_template(
        "shop.html",
        products=products
    )


# ================================
# Categories
# ================================

@app.route("/casual-wear")
def casual_wear():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products WHERE category = ?",
        ("Casual Wear",)
    ).fetchall()

    connection.close()

    return render_template(
        "casual_wear.html",
        products=products
    )

@app.route("/wedding-wear")
def wedding_wear():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products WHERE category = ?",
        ("Wedding Wear",)
    ).fetchall()

    connection.close()

    return render_template(
        "wedding_wear.html",
        products=products
    )

@app.route("/wedding-kids-wear")
def wedding_kids_wear():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products WHERE category = ?",
        ("Wedding Kids Wear",)
    ).fetchall()

    connection.close()

    return render_template(
        "wedding_kids_wear.html",
        products=products
    )


@app.route("/shalwar-materials")
def shalwar_materials():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products WHERE category = ?",
        ("Shalwar Materials",)
    ).fetchall()

    connection.close()

    return render_template(
        "shalwar_materials.html",
        products=products
    )


@app.route("/abayas")
def abayas():

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products WHERE category = ?",
        ("Abayas",)
    ).fetchall()

    connection.close()

    return render_template(
        "abayas.html",
        products=products
    )


# ================================
# Contact
# ================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ================================
# Run Application
# ================================

if __name__ == "__main__":
    app.run(debug=True)