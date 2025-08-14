import requests
from tkinter import *

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data['quote']

    words = quote.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + " " + word) <= 20:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    k_quotes = "\n".join(lines)

    canvas.itemconfig(kanye_quote, text=k_quotes)

#UI SETUP
window = Tk()
window.title("Kanye Says")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=300)
canvas_image = PhotoImage(file="quote-image.png")
canvas.create_image(150, 150,  image=canvas_image)
kanye_quote = canvas.create_text(150, 150, text="",
                                 font=("Helvetica", 12, "bold"),
                                 fill="black",
                                 width=200,
                                 justify="center")
canvas.grid(row=0, column=0)

k_image = PhotoImage(file="kanye-image.png")
kanye_button = Button(image=k_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()