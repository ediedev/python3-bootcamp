from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(600, 400)

# LABELS
my_label = Label(text="My Label", font=("Arial", 20, "bold"))
my_label.pack()

#entries
entry = Entry(width=30)
entry.insert(END, "Enter your value")
#getstext entry
print(entry.get())
entry.pack()

#text
text = Text(height=5, width=30)
#puts curser in text
text.focus()
#adds some text to begin with
text.insert(END, "Example of multi-line text entry")
#gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# spinbox
def spinbox_used():
    """prints the spinbox value"""
    #get the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scaled_value(value):
    """prints scaled value"""
    print(value)
scale = Scale(from_=0, to=100, command=scaled_value)
scale.pack()

#Checkbox
def checkbox_used():
    """prints 1 if On button checked, otherwise returns 0"""
    print(checked_state.get())
#variable to hold on to checked state, o is off, 1 is on
checked_state = IntVar()
checkbox = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbox.pack()

#Radiobutton
def radio_used():
    """prints 1 if On button checked, otherwise returns 0"""
    print(radio_state.get())
#variable to hold on to checked state, o is off, 1 is on
radio_state = IntVar()
radio_button1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

#Listbox
def listbox_used(event):
    """gets current selection from listbox"""
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["apple", "banana", "cherry", "Mango"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

#last of the code
window.mainloop()
