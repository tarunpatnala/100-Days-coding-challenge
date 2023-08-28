import random
# Loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit + " pie")

# Average height

#student_heights = input("Input a list of student heights ").split(", ")
student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
no_of_students = 0
for n in student_heights:
    total_height += n
    no_of_students += 1
print(round(total_height / no_of_students))

# Highest value
#student_scores = input("Input a list of student scores ").split(", ")
student_scores = [78, 65, 89, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
result = 0
for score in student_scores:
    if score > result:
        result = score
print(f"The highest score in the class is: {result}")

result = 0
for n in range(2,101,2):
    result += n

print(result)

for n in range(1, 101):
    if n%3 == 0 and n%5 ==0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)

# Final project password creator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"HOw many numbers would you like?\n"))
password = []
for char in range(1, nr_letters+1):
    password += random.choice(letters)

for char in range(1, nr_symbols+1):
    password += random.choice(symbols)

for char in range(1, nr_numbers+1):
    password += random.choice(numbers)

random.shuffle(password)
pwd = ""
for n in password:
    pwd += n
print(f"Your password is {pwd}")