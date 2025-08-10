from tkinter import *

FONT_NAME = "sans-serif"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(bg="white", padx=30, pady=30)

#canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.config(bg="white")
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=pass_img)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text="Website:", bg="white", font=FONT_NAME, padx=10, pady=10)
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white", font=(FONT_NAME, 12))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

#entries
web_entry = Entry(width=60)
web_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

#buttons
generate_btn = Button(text="Generate Password", font=(FONT_NAME, 12))
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", font=FONT_NAME, width=39)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()