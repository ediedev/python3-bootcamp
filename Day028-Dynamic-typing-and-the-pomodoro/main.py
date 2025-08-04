from tkinter import *

from PIL import ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg="white", padx=30, pady=30)
window.minsize(width=500, height=400)
canvas = Canvas(width=234, height=216)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(117,108, image=tomato_img)
canvas.pack()

window.mainloop()