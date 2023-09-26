from tkinter import Tk, Label, Button, Entry, END

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

e_mile = Entry()
e_mile.insert(END, string="0")
e_mile.grid(row=0, column=1)

l_miles = Label(text="Miles")
l_miles.grid(row=0, column=2)

l_equal = Label(text="is equal to")
l_equal.grid(row=2, column=0)

l_km_result = Label(text='0')
l_km_result.grid(row=1, column=1)

l_km = Label(text='Km')
l_km.grid(row=1, column=2)

def calculate():
    miles = float(e_mile.get())
    km = miles * 1.609
    l_km_result.config(text=f"{km:.2f}")

b_calculate = Button(text="Calculate", command=calculate)
b_calculate.grid(row=2, column=1)


window.mainloop()
