import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


def create_database_sqlite():
    db = sqlite3.connect("books-collection.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    db.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        hp = Book(title="Harry Potter", author="J. K. Rowling", rating=6)
        db.session.add(hp)
        db.session.commit()
