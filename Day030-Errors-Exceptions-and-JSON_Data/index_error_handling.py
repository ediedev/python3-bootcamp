from tkinter import messagebox

fruits = ["apple", "banana", "cherry"]

#catch the exception and make sure the code runs without crashing

def make_pie(index):
    """handles index errors"""
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit +" pie")

make_pie(5)
make_pie(1)