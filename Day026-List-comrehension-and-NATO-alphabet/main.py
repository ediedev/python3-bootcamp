import random

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#list comprehension with lists
#solution1: list comprehension
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

#solution2 : filtering even numbers
results = [ num for num in numbers if num%2==0]
print(results)

# solution3: data overlap
with open ("file1.txt") as file:
    file1 = file.readlines()

with open ("file2.txt") as file:
    file2 = file.readlines()

result = [int(num) for num in file1 if num in file2]
print(result)

#list comprehension with dictionaries (dictionary comprehension)
# generate random scores for students
students = ["Alex", "John", "Peter", "Robert", "Rogers"]

#dictionary comprehension for a list
student_scores = {student:random.randint(1,100) for student in students}
print(student_scores)

#dictionary comprehension for a dictionary
passed_students = {key:value for (key,value) in student_scores.items() if value > 60}
print(passed_students)

#solution4: calculates the number of letters in each word
words = ("You are going to use Dictionary Comprehension to create a dictionary called result "
         "that takes each word in the given sentence and calculates the number of letters in each word")

letter_count = {word:len(word) for word in words.split()}
print(letter_count)

#solution4: converts temperature in degrees Celsius into degrees Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# iterate over a pandas dataframe
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

#loop through a dataframe
for (key, value) in student_df.items():
    print(value)

#loop through rows of a dataframe
for (index, row) in student_df.iterrows():
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)