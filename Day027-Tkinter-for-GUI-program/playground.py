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