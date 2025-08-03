#returns the sum of any number of arguments

#*args
def add(*args):
    sums = 0
    for n in args:
        sums += n
    print(args[1])
    return sums

print(add( 2,3,4,5,6))

#**kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
print(calculate(2, add = 3, multiply = 5))

#create a class with **kwargs
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)

import tkinter as tk
root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 150, fill='blue')

# Draw a circle (oval)
canvas.create_oval(200, 50, 300, 150, fill='green')

# Draw a line
canvas.create_line(0, 0, 400, 300, fill='red', width=3)

# Add text
canvas.create_text(200, 200, text="Hello, Canvas!", font=("Arial", 16), fill='purple')

root.mainloop()
