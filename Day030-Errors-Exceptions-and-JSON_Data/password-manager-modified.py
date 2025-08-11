from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    letter_list = [choice(letters) for _ in range(randint(8,10))]
    symbol_list = [choice(symbols) for _ in range(randint(2,4))]
    number_list = [choice(numbers) for _ in range(randint(2,4))]

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
    new_data = {website:{"Email": email,
                        "Password": password}}

    if len(website) == 0 or len(email) < 16 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            #read the old data if data.json exists
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            #create a new data.json file
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #updata data with new_data
            data.update(new_data)
            #save the updated data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Saved", message="Saved Successfully.")
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()

def search_data():
    website = web_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.askokcancel(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
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
web_entry = Entry(width=34)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "e_name@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

#buttons
search_btn = Button(text="Search", font=FONT_NAME, width=16, bg="white", command=search_data)
search_btn.grid(column=2, row=1)
generate_btn = Button(text="Generate Password", font=FONT_NAME, bg="white",command=pass_generator )
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", font=FONT_NAME, width=39, bg="white", command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()

