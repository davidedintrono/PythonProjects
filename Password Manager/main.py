from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    pwd_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    email = mail_input.get()
    password = pwd_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                       f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("password.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            pwd_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)

mail_input = Entry(width=35)
mail_input.grid(column=1, row=2, columnspan=2)
mail_input.insert(0,"prova@prova.it")

pwd_label = Label(text="Password:")
pwd_label.grid(column=0, row=3)

pwd_input = Entry(width=21)
pwd_input.grid(column=1, row=3)

gen_pwd_button = Button(text="Generate Password", command=generate_password, width=10)
gen_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add, width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()