from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underscore(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello():
    return '<h1 style="text-align: center">Hello World!</h1>' \
        '<p>This is a paragraph<p>' \
        '<img src= "https://media.giphy.com/media/P2hdI6VaKlFhxncQG9/giphy.gif" width=480 height=308/>'


@app.route("/bye")
@make_bold
@make_italic
@make_underscore
def say_bye():
    return "Bye"

@app.route("/hello/<username>/<int:number>")
def great(username, number):
    return f"Hello {username} - {number}!"



if __name__ == "__main__":
    app.run(debug=True)
