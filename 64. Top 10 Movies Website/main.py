from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.UnicodeText)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.UnicodeText)
    img_url = db.Column(db.String)

class EditMovieRating(FlaskForm):
    rating = StringField("Your Rating ot of 10 eg. 7.5", validators=[validators.input_required()])
    review = StringField("Your Review", validators=[validators.input_required()])
    submit = SubmitField("Done")

class SearchMovie(FlaskForm):
    title = StringField("Movie Title", validators=[validators.input_required()])
    submit = SubmitField("Add Movie", validators=[validators.input_required()])

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(desc(Movie.ranking))).scalars()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = EditMovieRating()
    id = request.args.get('id', type=int)
    movie = db.get_or_404(Movie, id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect( url_for("home") )

    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete")
def delete():
    id = request.args.get("id", type=int)
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect( url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = SearchMovie()
    if form.validate_on_submit():
        title = form.title.data
        api_url = "https://imdb-api.com/en/API/SearchMovie/k_12345678/inception 2010"
        params = {"t": title}
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        movies = response.json()
        return url_for("select.html", movies=movies)
    
    return render_template("add.html", form=form)

def add_movies():
    new_movie1 = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

    second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg")

    with app.app_context():
        # db.session.add(new_movie1)
        db.session.add(second_movie)
        db.session.commit()

if __name__ == '__main__':
    # add_movies()
    app.run(debug=True)
