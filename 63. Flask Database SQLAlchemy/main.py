from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id =  db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()

        return redirect( url_for('home') )
    
    return render_template("add.html")

@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
    id = request.args.get('id', type = int)
    book = db.get_or_404(Book, id)

    if request.method == "POST":
        new_rating = float(request.form["rating"])
        book.rating = new_rating
        db.session.commit()

        return redirect( url_for('home'))
    
    return render_template("edit.html", book=book)

@app.route("/delete")
def delete():
    id = request.args.get("id", type=int)
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect( url_for("home") )

if __name__ == "__main__":
    app.run(debug=True)
