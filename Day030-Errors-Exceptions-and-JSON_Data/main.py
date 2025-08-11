try:
    file = open("my_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary)
except FileNotFoundError:
    file = open("my_file.txt", "w")
    file.write("Hello World")
except Exception as e:
    print(f"The key {e} was not found.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

#Create our own exceptions
# we use the keyword raise
height = int(input("Height: "))#in meters
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height must not be greater than 3")

bmi = weight / (height * height)
print(f"BMI: {bmi}")