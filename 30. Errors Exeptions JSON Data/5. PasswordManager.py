import random
import json
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, messagebox

DB_NAME = "password_database.json"

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
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(website_entry, email_entry, password_entry):
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Fill all fields", message="Please don't leave any field empty!")
    else:
        try:
            with open(DB_NAME, encoding="utf8", mode="r") as db:
                # Reading old data
                data = json.load(db)
        except FileNotFoundError:
            with open(DB_NAME, encoding="utf8", mode="w") as db:
                json.dump(new_data, db, indent=4)
        else:
            # Updating old data with new one
            data.update(new_data) #Konieczne, żeby zapisał nowe dane jako dodatkow wpis w pliku, inaczej dopisz nowe w sposób generujący błąd
        
            with open(DB_NAME, encoding="utf8", mode="w") as db:
                # Saving the updated data
                json.dump(data, db, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            generate_password(password_entry)
            website_entry.focus()

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password(website_entry):
    try:
        with open(DB_NAME, encoding="utf8", mode="r") as db:
            # Reading old data
            data = json.load(db)
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message=f"No data for the website {website_entry.get()} exists")
    else:
        if website_entry.get() in data.keys():
            found_data = data[website_entry.get()]
            messagebox.showinfo(title=website_entry.get(), message=f"email: {found_data['email']}\nPassword: {found_data['password']}")
        else:
            messagebox.showinfo(title="Info", message=f"No data for the website {website_entry.get()} exists")
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

e_website = Entry(width=21)
e_website.grid(column=1, row=1)
e_website.focus()

e_email = Entry(width=35)
e_email.grid(column=1, row=2, columnspan=2)
e_email.insert(0, "user@e-mail.pl")

e_password = Entry(width=21)
generate_password(e_password)
e_password.grid(column=1, row=3)

b_search = Button(text="Search", command= lambda: search_password(e_website))
b_search.grid(column=2, row=1)

b_generate = Button(text="Generate Password", command= lambda: generate_password(e_password))
b_generate.grid(column=2, row=3)

b_add = Button(text="Add", width=36, command= lambda: save_password(e_website, e_email, e_password))
b_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
