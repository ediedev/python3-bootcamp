from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "sans-serif"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    """Generates a password of given length"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #comprehension lists
    letter_list = [choice(letters) for char in range(randint(8,10))]
    symbol_list = [choice(symbols) for symbol in range(randint(2,4))]
    number_list = [choice(numbers) for num in range(randint(2,4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

    pyperclip.copy(password)#copies the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) < 16 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Save?", message=f"These are the details entered:\n"
                                                  f"Website: {website}\n Email: {email}\n "
                                                  f"Password: {password}\n Is it Ok to save?")
        if is_ok:
            file_link = "data.txt"
            with open(file_link, "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                messagebox.showinfo(title="Saved!", message=f"Saved successfully! to {file_link}")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(bg="white", padx=30, pady=30)
window.grid_rowconfigure(3, minsize=40)

#canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.config(bg="white")
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=pass_img)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text="Website:", bg="white", font=FONT_NAME, padx=10, pady=10)
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white", font=FONT_NAME)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", font=FONT_NAME)
password_label.grid(column=0, row=3)

#entries
web_entry = Entry(width=60)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "e_name@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

#buttons
generate_btn = Button(text="Generate Password", font=FONT_NAME, bg="white",command=pass_generator )
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", font=FONT_NAME, width=39, bg="white", command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()