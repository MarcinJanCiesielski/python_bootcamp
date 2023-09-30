import csv
import random
from tkinter import Button, Canvas, PhotoImage, Tk

word_list = []
LANGUAGE_TO_LEARN = "French"
LANGUAGE_MAIN = "English"
BACKGROUND_COLOR = "#B1DDC6"

def read_data():
    try:
        with open("./data/words_to_learn.csv", "r") as wtl:
            data = csv.DictReader(wtl)
            return [row for row in data]
    except FileNotFoundError:
        with open("./data/french_words.csv", mode="r") as f:
            data = csv.DictReader(f)
            return [row for row in data]

def save_progress(words_to_learn):
    with open("./data/words_to_learn.csv", "w") as wtl:
        fieldnames = [LANGUAGE_TO_LEARN, LANGUAGE_MAIN]
        writer = csv.DictWriter(wtl, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(words_to_learn)

def next_card(canva):
    global flip_timer

    window.after_cancel(flip_timer)
    word = generate_word()
    canva.itemconfig(l_language, text=LANGUAGE_TO_LEARN, fill="black")
    canva.itemconfig(l_word, text=f"{word[LANGUAGE_TO_LEARN]}", fill="black")
    flip_timer = window.after(3000, func=lambda: flip_card(canvas, word))
    return word
    
def flip_card(canva, word):
    global i_card_back
    canva.itemconfig(l_language, text=LANGUAGE_MAIN, fill="white")
    canva.itemconfig(l_word, text=f"{word[LANGUAGE_MAIN]}", fill="white")
    canva.itemconfig(canvas_background, image=i_card_back)

def generate_word():
    return random.choice(word_list)

def wright_answer(canva, word):
    global word_list
    for i in range(len(word_list)):
        if word_list[i][LANGUAGE_TO_LEARN] == word[LANGUAGE_TO_LEARN]:
            del word_list[i]
            break
    save_progress(word_list)
    next_card(canva)

def wrong_answer(canva):
    next_card(canva)

word_list = read_data()

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=lambda: flip_card(canvas, current_word))

i_card_front = PhotoImage(file="./images/card_front.png")
i_card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(400, 263, image=i_card_front)
l_language = canvas.create_text(400, 150, text="Language", font=("Ariel",40, "italic" ))
l_word = canvas.create_text(400, 263, text="Word", font=("Ariel",60, "bold" ))
current_word = next_card(canvas)
canvas.grid(column=0, row=0, columnspan=2)

i_right = PhotoImage(file="./images/right.png")
b_wright = Button(command=lambda: wright_answer(canvas, current_word), image=i_right)
b_wright.grid(column=0, row=1)

i_wrong = PhotoImage(file="./images/wrong.png")
b_wrong = Button(command=lambda: wrong_answer(canvas), image=i_wrong)
b_wrong.grid(column=1, row=1)



window.mainloop()
