# Randomisation 

import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

head_tail = random.randint(0,1)
if head_tail == 1:
    print("Heads")
else:
    print("Tails")


# Lists

states_of_america = ["Deleware", "Pennsylvania"]

text = "Agela, Ben, Jenny"
names = text.split(", ")
#value = random.randint(0, len(names)-1)
#print(names[value])
result = random.choice(names)
print(result)

values = [1,2,5,7,3,4]
values.pop()
values.remove(1)
values.sort()
print(values)
values.clear()
print(values)
values.extend([8,9])
print(values)

#Multiple lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])

#Treasure map
row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]
map = [row1, row2, row3]
value = input("Enter two digits: ")
column = int(value[0])-1
row = int(value[1])-1
map[column][row] = "Y"
print(f"{row1}\n{row2}\n{row3}")

#Rock paper and scissors
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game = [rock, paper, scissors]
computer = random.randint(0,2)
user = int(input("What do you choose? Type 0 for Rick, 1 for Paper or 2 for Scissors.\n"))
if user>=3 or user <0:
    print("You have entered invalid number, you loose!")
else:
    print(f"You have choosen:\n{game[user]}")
    print(f"Computer choose:\n{game[computer]}")

    if user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You loose!")
    elif computer > user:
        print("You loose!")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("It's a draw")