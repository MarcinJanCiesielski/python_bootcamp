import datetime
import random

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.date.today().strftime("%Y")
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    lower_name = name.lower()
    age_response = requests.get(f"https://api.agify.io?name={lower_name}", timeout=20)
    age_response.raise_for_status()
    guessed_age = age_response.json()['age']

    sex_response = requests.get(f"https://api.genderize.io/?name={lower_name}", timeout=20)
    sex_response.raise_for_status()
    guessed_sex = sex_response.json()["gender"]

    return render_template("guess.html", name=name.title(), sex=guessed_sex, age=guessed_age)

@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391", timeout=20)
    response.raise_for_status()
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run()
