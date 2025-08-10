from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """starts the timer"""
    global reps
    reps += 1
    reps %= 4

    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """counts down once the start button is pressed"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg="white", padx=100, pady=50)
window.minsize(width=500, height=400)

# timer
my_timer = Label(text="Timer", fg=GREEN,bg="white", font=(FONT_NAME, 30, "bold"))
my_timer.grid(column=2, row=0)

#tomato image
canvas = Canvas(width=226, height=211, highlightthickness=0)
canvas.config(bg="white")
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(114,106, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# start
my_start = Button(text="Start", font=(FONT_NAME, 14, "bold"), command=start_timer)
my_start.grid(column=1, row=3)

# Reset
my_reset = Button(text="Reset", font=(FONT_NAME, 14, "bold"))
my_reset.grid(column=3, row=3)

# check
my_check = Label(text="✔", bg="white", fg=GREEN, font=("Arial", 20, "bold"))
my_check.grid(column=2, row=4)


window.mainloop()