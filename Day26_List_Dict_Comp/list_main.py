lst = (1, 2, 3)
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
print([l + 1 for l in lst])
print([i * 2 for i in range(1, 6)])
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print([n ** 2 for n in numbers])
print([n for n in numbers if n%2==0])

name = "Tarun"
#name = input("Enter your name: ")
name_dict = {"a": "Alfa", "b": "Broccoli", "c": "California", "d": "Denmark", "e": "Elephant", "f": "France",
             "g": "Goa", "h": "Hong kong", "i": "Italy", "j": "Joker", "k": "Kerala", "l": "London", "m": "Mumbai",
             "n": "New York", "o": "Orange", "p": "Pakistan", "q": "Queen", "r": "Rose", "s": "Sand", "t": "Tokyo",
             "u": "Umbrella", "v": "Van", "w": "Wok", "x": "Xerox", "y": "Yack", "z": "Zoo"}
print([name_dict[n.lower()] for n in name.replace(" ", "") if
       all(x.lower() in name_dict.keys() for x in name.replace(" ", ""))])


with open("file1.txt") as file1:
    data1 = file1.read().split("\n")

with open("file2.txt") as file2:
    data2 = file2.read().split("\n")

result = [int(d) for d in data1 if d in data2]
print(result)
