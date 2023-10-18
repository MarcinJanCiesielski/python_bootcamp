import random
from flask import Flask

app = Flask(__name__)

number_to_guess = random.randint(0, 9)
print(number_to_guess)

@app.route("/")
def game():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:user_number>")
def user_number(user_number):
    if number_to_guess == user_number:
        return '<h1 style="color: green">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    if user_number > number_to_guess:
        return '<h1 style="color: purple">Too high! Try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    if user_number < number_to_guess:
        return '<h1 style="color: red">Too low! Try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'

if __name__ == "__main__":
    app.run()
