from tkinter import *
import pandas as pd
import random

BG_COLOR = "#B1DDC6"
current_card = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/french_words.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")
    current_card = {}

def next_card():
    """moves to the next card and flips after 3 minutes if the French word is unknown"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    """Flips to the English word"""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=new_image)

def is_known():
    """Saves unknown French words to a csv file"""
    to_learn.remove(current_card)
    data = (pd.DataFrame(to_learn))
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50, bg=BG_COLOR)
flip_timer = window.after(3000, flip_card)

#canvas and cards
canvas = Canvas(width=366, height=260)
old_image = PhotoImage(file="images/front-card.png")
new_image = PhotoImage(file="images/back-card.png")
canvas_image = canvas.create_image(183,130, image=old_image)
card_title = canvas.create_text(183,80, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(183,150, text="", font=("Arial", 50 , "bold"))

canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(bg=BG_COLOR, image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(bg=BG_COLOR, image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()