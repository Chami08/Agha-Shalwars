from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/casual-wear")
def casual_wear():
    return render_template("casual_wear.html")

@app.route("/wedding-wear")
def wedding_wear():
    return render_template("wedding_wear.html")

@app.route("/wedding-kids-wear")
def wedding_kids_wear():
    return render_template("wedding_kids_wear.html")

@app.route("/shalwar-materials")
def shalwar_materials():
    return render_template("shalwar_materials.html")

@app.route("/abayas")
def abayas():
    return render_template("abayas.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)