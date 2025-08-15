from question_model import Question
from quiz_brain import QuizBrain
import requests
from tkinter import *

BG_COLOR = "#B1DDC6"
def get_random_question():
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()

    question_data = response.json()["results"]

    question_bank = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()
    print("You have completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50, bg=BG_COLOR)
# flip_timer = window.after(3000, flip_card)

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
unknown_button = Button(bg=BG_COLOR, image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(bg=BG_COLOR, image=check_image, highlightthickness=0, command=get_random_question)
known_button.grid(column=1, row=1)

window.mainloop()