from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """resets timer and other variables"""
    global timer
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    # ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """starts the timer"""
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        timer_label["fg"] = RED
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        timer_label["fg"] = PINK
    else:
        count_down(work_sec)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """counts down once the start button is pressed"""
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_label.config(text=f"{len(marks)}✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg="white", padx=100, pady=50)
window.minsize(width=500, height=400)

# timer
timer_label = Label(text="Timer", fg=GREEN,bg="white", font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2, row=0)

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
my_reset = Button(text="Reset", font=(FONT_NAME, 14, "bold"), command=reset_timer)
my_reset.grid(column=3, row=3)

# check
check_label = Label(bg="white", fg=GREEN, font=("Arial", 20, "bold"))
check_label.grid(column=2, row=4)

window.mainloop()