from flask import Flask, render_template
from post import Post
from utils import getCurrentYear
import json
import os


data_file_path = os.path.join(os.path.dirname(__file__), 'data', 'data.json')
with open(data_file_path, 'r', encoding='utf-8') as file:
    posts = json.load(file)

post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, currentYear=getCurrentYear())


@app.route("/about")
def about():
    return render_template("about.html", currentYear=getCurrentYear())


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, currentYear=getCurrentYear())


def init_server():
    app.run(debug=True)
