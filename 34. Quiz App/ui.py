from tkinter import Tk, Button, Canvas, Label, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)

        true_i = PhotoImage(file="./images/true.png")
        self.true_b = Button(image=true_i, highlightthickness=0, command=self.answer_true)
        self.true_b.grid(column=0, row=2)

        false_i = PhotoImage(file="./images/false.png")
        self.false_b = Button(image=false_i, highlightthickness=0, command=self.answer_false)
        self.false_b.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.score.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached to the end of the game!")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")


    def answer_true(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

