import requests
from flask import Flask, render_template


def get_blog_posts():
    data_url="https://api.npoint.io/eb6cd8a5d783f501ee7d"

    response = requests.get(data_url, timeout=20)
    response.raise_for_status()
    return response.json()

blog_posts = get_blog_posts()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/show_post/<int:p_id>")
def show_post(p_id):
    post_to_view = blog_posts[p_id - 1]
    return render_template("post.html", post=post_to_view, image_url=post_to_view['image_url'])

if __name__ == "__main__":
    app.run()
