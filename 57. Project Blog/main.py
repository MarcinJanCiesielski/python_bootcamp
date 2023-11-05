from flask import Flask, render_template
import requests
from post import Post

def get_blog_data() -> list:
    blog_data_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_data_url, timeout=20)
    response.raise_for_status()
    all_posts = response.json()

    posts = [Post(p["id"], p["title"], p["subtitle"], p["body"]) for p in all_posts]

    return posts

blog_posts = get_blog_data()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/post/<post_id>")
def post(post_id):
    chosen_post = get_post(int(post_id))
    return render_template("post.html", post=chosen_post)



def get_post(id: int) -> Post:
    for post in blog_posts:
        if post.id == id:
            return post

if __name__ == "__main__":
    app.run(debug=True)
