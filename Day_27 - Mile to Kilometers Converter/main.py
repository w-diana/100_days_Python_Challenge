import tkinter
from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    output = round(miles * 1.609, 2)
    output_label.config(text=output)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=25)

result = 0

# arrange all the widgets
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)

output_label = Label(text=result)
output_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# keeps the GUI open
window.mainloop()