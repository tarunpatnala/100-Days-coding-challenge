print("Hello"[0:-1])
print(123_345_567+2) # _ is treated as , 

#BMI = weight(KG) / height(m) * height (m)
#data manipulation
height = input("Enter your height in m: ")
weight = input("Enter your weight in KG: ")
BMI = float(weight) / float(height)**2
print(round(BMI,2))
BMI = float(weight) // float(height)**2 #// returns integer instead of float.
print(BMI)
#f-string
print(f"Your score is {BMI} based on your height which is {height} and your weight which is {weight}")

#Life caculator
age = input("What is your current age? ")
age_years = 90 - int(age)
age_months = age_years *12
age_weeks = age_years * 52
age_days = age_years * 365
print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")

# Final project 
# Tip calculator
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_number = input("How many people to split the bill? ")
result = (float(total_bill[1:]) / int(split_number)) * (1+int(tip_percentage)/100)
bill = "{:.2f}.format(result)"
print(f"Each person should pay: ${bill}")