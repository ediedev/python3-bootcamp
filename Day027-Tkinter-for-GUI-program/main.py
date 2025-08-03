from tkinter import *

def button_clicked():
    """Updates my_label with new value"""
    new_text = inputs.get()
    my_label["text"] = new_text

window = Tk()
window.title("My First GUI Program")
window.minsize(600, 400)
window.config(padx=20, pady=20)
# Label
my_label = Label(text="My Label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)

#button
button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

#button
button1 = Button(text="New Button", command=button_clicked)
button1.grid(column=3, row=0)

#entry
inputs = Entry(width=20)
print(inputs.get())
inputs.grid(row=3, column=4)




#last of the code
window.mainloop()


