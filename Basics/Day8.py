import math as m
# Function parameters
def greet(name, location):
    print(f"Hello! {name}")
    print("How you doing?")
    print(f"Isn't the weather nice today in {location}?")

greet("Tarun", "Sydney")
greet("Varun", "Melbourne")
# Keyword arguments
greet(location="Perth", name="Rahul")


def paint_calc(h,w,c):
    r = (h*w) / c
    return m.ceil(r)

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 5
result = paint_calc(h=height, w=width, c=coverage)
print(f"You will need {result} cans to paint the wall.")

# Prime checker
def prime_checker(n):
    is_prime = True
    for i in range(2, n):
        if n%i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(n)

#Caeser cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
            shift *= -1
    for i in text:
        if i in alphabet:
            x = alphabet.index(i)
            result += alphabet[x+shift]
        else:
            result += i
    print(f"The {direction}d text is {result}")

#def encrypt(text, shift):
#    result = ""
#    for i in text:
#        x = alphabet.index(i)
#        result += alphabet[x+shift]
#    print(f"The encoded text is {result}")
#def decrypt(text, shift):
#    result = ""
#    for i in text:
#        x = alphabet.index(i)
#        result += alphabet[x-shift]
#    print(f"The encoded text is {result}")

print(logo)

end_loop=False
while not end_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(text, shift, direction)
    retry = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if retry == "no":
        print("Good bye!")
        end_loop = True