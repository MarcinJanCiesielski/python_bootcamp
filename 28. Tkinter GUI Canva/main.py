from tkinter import Tk, Canvas, PhotoImage, Label, Button
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer, l_check_marks, l_work_break_indicator, canvas

    window.after_cancel(timer)
    l_check_marks.config(text="")
    l_work_break_indicator.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, l_work_break_indicator
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        l_work_break_indicator.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        l_work_break_indicator.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        l_work_break_indicator.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, l_check_marks
    mins = count // 60
    secs = count % 60
    if mins < 10:
        mins = f"0{mins}"

    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            l_check_marks.config(text=f"{(reps/2) * CHECK_MARK}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

l_work_break_indicator = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"))
l_work_break_indicator.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

b_start = Button(text="Start", command=start_timer, highlightthickness=0)
b_start.grid(row=2, column=0)


b_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
b_reset.grid(row=2, column=2)

l_check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 13, "bold"))
l_check_marks.grid(row=3, column=1)

window.mainloop()

