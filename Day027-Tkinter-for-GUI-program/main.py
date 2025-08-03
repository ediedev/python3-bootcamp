from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(600, 400)

# LABELS
my_label = Label(text="My Label", font=("Arial", 20, "bold"))
my_label.pack()

# #update label text
# #either
# my_label["text"] = "New Text1"
# #or
# my_label.config(text="New Text2")

# BUTTONS

def button_clicked():
    """Updates my_label with new value"""
    new_text = inputs.get()
    my_label["text"] = new_text

button = Button(text="Click Me", command=button_clicked)
button.pack()

#ENTRY
inputs = Entry(width=20)
inputs.pack()


#last of the code
window.mainloop()


