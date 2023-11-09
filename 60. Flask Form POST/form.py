import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("form.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        login = request.form["username"]
        pswd = request.form["password"]
        text = f"Name:{login}, Password:{pswd}"
        return render_template("login.html", text_to_view=text)

if __name__ == "__main__":
    app.run()
