import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mycreation")
def mycreation():
    return render_template("mycreation.html")


@app.route("/offer")
def offer():
    return render_template("offer.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/base")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)