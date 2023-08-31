#Dictionaries
programming_dictionary = {"Bug":"An error in a program that prevents the program from running as expected.", "Function":"A piece of code that you can easily call over and over again.", "Loop":"The action of doing something over and over again."}

print(programming_dictionary["Bug"])

programming_dictionary["Dict"]=[1,"asd", 12.12]

print(programming_dictionary)

programming_dictionary["Bug"]="This is also called as an issue"

print(programming_dictionary)
print("================================")
for thing in programming_dictionary:
    print(programming_dictionary[thing])

print("================================")

#Tokenisation #Concrete syntax Trees #Abstract syntax Trees #Bytcode #Python Virtual Machine

student_scores={"Harry":83, "Ron":78, "Hermione":99, "Draco":74, "Neville":62}

for key in student_scores:
    score = student_scores[key]
    if score > 91:
        student_scores[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_scores[key] = "Exceeds Expectation"
    elif score >= 71 and score <= 80:
        student_scores[key] = "Acceptable"
    elif score <= 70:
        student_scores[key] = "Fail"

print("\n".join("{}:{}".format(k,student_scores[k]) for k in student_scores))

#Nested dictionary

nDict = {
    "France":{"cities_visited":["Paris","Lille","Dijon"], "total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visits":5}
}

travel_log = [
    {"country":"France","cities_visited":["Paris","Lille","Dijon"], "total_visits": 12},
    {"country":"Germany","cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visits": 5}
]

def add_new_country(country,total_visits,cities_visited):
    new_country={}
    new_country["country"] = country
    new_country["total_visits"] = total_visits
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia",2,["Moscow","Saint Peters"])

print(travel_log)

#Blind Bid
logo = '''
   ___________
   \         /
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
   /_________\
   `'-------'`
 .-------------.
/_______________\
'''
print(logo)
print("Welcome to the secret auction program.")
dict = {}
retry = False
while not retry:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dict[name]=bid
    response = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if response.lower() == "no":
        retry = True

def find_highest_bidder(bidding_record):
    val = 0
    winner = ""
    for name in dict:
        if dict[name] > val:
            val = dict[name]
            winner = name
    print(f"The final bid winner is {winner} with bid of ${val}")

find_highest_bidder(dict)