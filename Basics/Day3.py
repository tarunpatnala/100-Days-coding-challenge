# if condition:
# statement 
# else:
# statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age < 12:
        print("Please pay $15.")
    elif age <= 18:
        print("Please pay $17.")
    else:
        print("Please pay $20.")
else:
    print("Sorry, you have to grow taller before you can ride.")


number = int(input("Enter a number to check odd or even: "))
if number % 2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")

year = int(input("Which year do you want to check? "))
if (year%4==0 and year%100!=0):
    print("Year is a leap year")
elif(year%100 ==0 and year%400 ==0):
    print("Year is a leap year")
else:
    print("Year is NOT a leap year")

# Pizza
print("Welcome to Python pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}")

# Love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
calc = "truelove"
count = 0
for c in calc.lower():
    count += name1.count(c)
    count += name2.count(c)

if count < 10 or count > 90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count >= 40 and count <= 50:
    print(f"Your score is {count}, you are alright together")
else:
    print(f"Your score is {count}")

# Treasure island
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
input1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if input1 == "left":
    input2 = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if input2 == "wait":
        input3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if input3 == "blue":
            print("You entered a room of beasts. Game Over.")
        elif input3 == "red":
            print("You entered a room of Lions. Game Over.")
        elif input3 == "yellow":
            print('''
         __________
        /\____;;___\\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
        ''')
            print("***You found the treasure! You Win!***")
        else:
            print("You selected room of ghosts. Game Over.")
    else:
        print("You went out of breath. Game Over.")
else:
    print("You fell into a river. Game Over.")
