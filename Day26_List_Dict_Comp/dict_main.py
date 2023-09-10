import pandas
# new_dict = {new_key:new_value for (key,value) in dict_items() if test}

import random

students = ["Ross", "Rachel", "Monica", "Chandler", "Joey", "Phoebe"]
student_score = {student: random.randint(70, 90) for student in students}
print(student_score)
students_passed = {student: score for (student, score) in student_score.items() if score > 80}
print(students_passed)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (value * 9 / 5) + 32 for (day, value) in weather_c.items()}
print(weather_f)

student_data = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataFrame = pandas.DataFrame(student_data)
for (index, row) in student_dataFrame.iterrows():
    if row.students == "Angela":
        print(row.score)

dictionary = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in dictionary.iterrows()}
name = "Tarun"
name_list = [nato_dict[n] for n in name.upper() if n in nato_dict.keys()]
print(name_list)
