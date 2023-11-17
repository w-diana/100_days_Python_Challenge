from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

BLUE = "#00A9FF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Choose randomly the no. of letters, symbols and numbers requested
    password_letters = [choice(letters) for _ in range(0, randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(0, randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(0, randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    # Convert the password list to a string
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered: \nEmail: {email_entry.get()} "
                                               f"\nPassword: {password_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            reset()


# ---------------------------- RESET ENTRY'S ------------------------------- #
def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", fg="black", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)

# Entry's
website_entry = Entry(width=35, fg="black", bg="white", highlightthickness=1, insertbackground="black",
                      highlightcolor=BLUE, highlightbackground="white")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=1, insertbackground="black",
                    highlightcolor=BLUE, highlightbackground="white")
email_entry.insert(0,"wapei@yahoo.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=1, insertbackground="black",
                       highlightcolor=BLUE, highlightbackground="white")
password_entry.grid(row=3, column=1)

# Buttons
add_button = Button(text="Add", width=36, highlightbackground="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
generate_password_button = Button(text="Generate Password", highlightbackground="white", command=generate_password)
generate_password_button.grid(row=3, column=2)

window.mainloop()
