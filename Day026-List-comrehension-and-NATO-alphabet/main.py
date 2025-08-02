numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

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
