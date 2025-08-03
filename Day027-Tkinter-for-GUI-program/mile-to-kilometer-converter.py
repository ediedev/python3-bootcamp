from tkinter import *

def button_clicked():
    """Updates my_label with new value"""
    mile = float(inputs.get())
    kms = round(mile * 1.61)
    value["text"] = kms

window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(300, 200)
window.config(padx=30, pady=30)

#miles input
inputs = Entry(width=10)
inputs.insert(END, "0")
print(inputs.get())
inputs.grid(row=0, column=3)

#miles
miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=4, row=0)
miles.config(padx=10,pady=10)

#miles
equal = Label(text="is equal to", font=("Arial", 12, "bold"))
equal.grid(column=2, row=2)
equal.config(padx=10, pady=10)

#value
value = Label(text="0", font=("Arial", 12, "bold"))
value.grid(column=3, row=2)

#km
km = Label(text=" Km", font=("Arial", 12, "bold"))
km.grid(column=4, row=2)
#button
button = Button(text="Button", command=button_clicked)
button.grid(column=3, row=3)






#last of the code
window.mainloop()


