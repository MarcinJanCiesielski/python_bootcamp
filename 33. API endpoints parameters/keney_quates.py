from tkinter import Canvas, Tk, Button, PhotoImage
import requests


def get_quote(canva):
    response = requests.get("https://api.kanye.rest", timeout=20)
    response.raise_for_status()
    quote = response.json()["quote"]
    canva.itemconfigure(quote_text, text=quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote(canvas)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=lambda: get_quote(canvas))
kanye_button.grid(row=1, column=0)



window.mainloop()
