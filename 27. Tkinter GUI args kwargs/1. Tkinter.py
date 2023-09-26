from tkinter import Tk, Label, Button, Entry

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # add padding

# Label
my_label = Label(text="I'm a label", font=("Roboto", 24, "bold"))
# my_label.pack() # dołącza etykietę do okna
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

# Button
def button_clicked():
    my_label.config(text=input_entry.get())


button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

# Entry - Input
input_entry = Entry(width=15)
input_entry.grid(row=2, column=3)

button2 = Button(text="New Button")
button2.grid(row=0, column=2)

window.mainloop()
