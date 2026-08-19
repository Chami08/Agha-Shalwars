from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
import os
import uuid


app = Flask(__name__)

app.secret_key = "agha-shalwars-secret-key"


# ================================
# Image Upload Settings
# ================================

UPLOAD_FOLDER = "static/images/products"

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


def save_uploaded_image(file):

    if not file or file.filename == "":
        return None

    if not allowed_file(file.filename):
        return None

    # Create folder if it does not exist
    os.makedirs(
        app.config["UPLOAD_FOLDER"],
        exist_ok=True
    )

    # Get original extension
    extension = file.filename.rsplit(".", 1)[1].lower()

    # Create unique filename
    filename = f"{uuid.uuid4().hex}.{extension}"

    # Full path
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    # Save image
    file.save(filepath)

    # Path stored in database
    return "images/products/" + filename


# ================================
# Database Connection
# ================================

def get_db_connection():

    connection = sqlite3.connect("shop.db")

    connection.row_factory = sqlite3.Row

    return connection


# ================================
# Admin Login
# ================================

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        connection = get_db_connection()

        admin = connection.execute(
            "SELECT * FROM admins WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if admin and check_password_hash(
            admin["password"],
            password
        ):

            session["admin_logged_in"] = True

            session["admin_username"] = admin["username"]

            return redirect(
                url_for("admin_dashboard")
            )

        else:

            return render_template(
                "admin_login.html",
                error="Invalid username or password."
            )

    return render_template("admin_login.html")


# ================================
# Admin Logout
# ================================

@app.route("/admin/logout")
def admin_logout():

    session.clear()

    return redirect(
        url_for("admin_login")
    )


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
# Casual Wear
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


# ================================
# Wedding Wear
# ================================

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


# ================================
# Wedding Kids Wear
# ================================

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


# ================================
# Shalwar Materials
# ================================

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


# ================================
# Abayas
# ================================

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

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        message = request.form["message"]

        connection = sqlite3.connect("shop.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO submissions
            (name, email, phone, subject, message)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, subject, message))

        connection.commit()
        connection.close()

        return render_template(
            "contact.html",
            success="Your message has been submitted successfully!"
        )

    return render_template("contact.html")

# ================================
# Admin Submissions
# ================================

@app.route("/admin/submissions")
def admin_submissions():

    if not session.get("admin_logged_in"):
        return redirect(
            url_for("admin_login")
        )

    connection = get_db_connection()

    submissions = connection.execute(
        "SELECT * FROM submissions ORDER BY created_at DESC"
    ).fetchall()

    connection.close()

    return render_template(
        "submissions.html",
        submissions=submissions
    )

# ================================
# Admin Dashboard
# ================================

@app.route("/admin")
def admin_dashboard():

    if not session.get("admin_logged_in"):

        return redirect(
            url_for("admin_login")
        )

    connection = get_db_connection()

    total_products = connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()[0]

    in_stock = connection.execute(
        "SELECT COUNT(*) FROM products WHERE stock > 0"
    ).fetchone()[0]

    out_of_stock = connection.execute(
        "SELECT COUNT(*) FROM products WHERE stock = 0"
    ).fetchone()[0]

    connection.close()

    return render_template(
        "admin_dashboard.html",
        total_products=total_products,
        in_stock=in_stock,
        out_of_stock=out_of_stock
    )


# ================================
# Add Product
# ================================

@app.route("/admin/add-product", methods=["GET", "POST"])
def add_product():

    if not session.get("admin_logged_in"):

        return redirect(
            url_for("admin_login")
        )

    if request.method == "POST":

        name = request.form["name"]

        category = request.form["category"]

        price = request.form["price"]

        description = request.form["description"]

        sizes = request.form["sizes"]

        stock = request.form["stock"]


        # ================================
        # Upload Image
        # ================================

        file = request.files.get("image")

        image = save_uploaded_image(file)


        if image is None:

            return (
                "Please upload a valid JPG, JPEG, PNG or WEBP image.",
                400
            )


        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO products
            (
                name,
                category,
                price,
                description,
                image,
                sizes,
                stock
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                category,
                price,
                description,
                image,
                sizes,
                stock
            )
        )

        connection.commit()

        connection.close()

        return redirect(
            url_for("manage_products")
        )

    return render_template(
        "add_product.html"
    )


# ================================
# Manage Products
# ================================

@app.route("/admin/products")
def manage_products():

    if not session.get("admin_logged_in"):

        return redirect(
            url_for("admin_login")
        )

    connection = get_db_connection()

    products = connection.execute(
        "SELECT * FROM products ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template(
        "manage_products.html",
        products=products
    )


# ================================
# Edit Product
# ================================

@app.route(
    "/admin/edit-product/<int:product_id>",
    methods=["GET", "POST"]
)
def edit_product(product_id):

    if not session.get("admin_logged_in"):

        return redirect(
            url_for("admin_login")
        )


    connection = get_db_connection()

    product = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()


    if product is None:

        connection.close()

        return "Product not found", 404


    # ================================
    # Update Product
    # ================================

    if request.method == "POST":

        name = request.form["name"]

        category = request.form["category"]

        price = request.form["price"]

        description = request.form["description"]

        sizes = request.form["sizes"]

        stock = request.form["stock"]


        # Keep existing image
        image = product["image"]


        # ================================
        # Check New Image
        # ================================

        file = request.files.get("image")


        if file and file.filename != "":

            new_image = save_uploaded_image(file)


            if new_image is None:

                connection.close()

                return (
                    "Invalid image type. "
                    "Please upload JPG, JPEG, PNG or WEBP.",
                    400
                )


            image = new_image


        # ================================
        # Update Database
        # ================================

        connection.execute(
            """
            UPDATE products

            SET name = ?,
                category = ?,
                price = ?,
                description = ?,
                image = ?,
                sizes = ?,
                stock = ?

            WHERE id = ?
            """,
            (
                name,
                category,
                price,
                description,
                image,
                sizes,
                stock,
                product_id
            )
        )


        connection.commit()

        connection.close()


        return redirect(
            url_for("manage_products")
        )


    connection.close()


    return render_template(
        "edit_product.html",
        product=product
    )


# ================================
# Delete Product
# ================================

@app.route(
    "/admin/delete-product/<int:product_id>"
)
def delete_product(product_id):

    if not session.get("admin_logged_in"):

        return redirect(
            url_for("admin_login")
        )


    connection = get_db_connection()


    # Get image before deleting product
    product = connection.execute(
        "SELECT image FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()


    # Delete product
    connection.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )


    connection.commit()

    connection.close()


    return redirect(
        url_for("manage_products")
    )


# ================================
# Run Application
# ================================

if __name__ == "__main__":

    app.run(debug=True)