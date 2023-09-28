import random
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(password_entry):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(website_entry, email_entry, password_entry):
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Fill all fields", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:\ne-mail\\user: {email_entry.get()}\nPassword: {password_entry.get()}\nis it OK to save?")

        if is_ok:
            with open("pasword_database.txt",encoding="utf8", mode="a") as db:
                db.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            generate_password(password_entry)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

l_website = Label(text="Website:")
l_website.grid(column=0, row=1)

l_email = Label(text="e-mail/Username")
l_email.grid(column=0, row=2)

l_pass = Label(text="Password")
l_pass.grid(column=0, row=3)

e_website = Entry(width=35)
e_website.grid(column=1, row=1, columnspan=2)
e_website.focus()

e_email = Entry(width=35)
e_email.grid(column=1, row=2, columnspan=2)
e_email.insert(0, "user@e-mail.pl")

e_password = Entry(width=21)
generate_password(e_password)
e_password.grid(column=1, row=3)

b_generate = Button(text="Generate Password", command= lambda: generate_password(e_password))
b_generate.grid(column=2, row=3)

b_add = Button(text="Add", width=36, command= lambda: save_password(e_website, e_email, e_password))
b_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
