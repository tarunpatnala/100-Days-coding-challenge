# import csv
# with open("weather_data.csv") as weather:
#     output = csv.reader(weather)
#     temperature = []
#     for out in output:
#         if out[1] == "temp":
#             continue
#         temperature.append(int(out[1]))
#
# print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
temp = data["temp"].to_list()
print(data["temp"].mean())
print(data["temp"].max())
print(data.temp.to_list())
print(data.temp.get(0))

print(data[data.day == "Monday"].condition[0])
print((data[data.day == "Monday"].temp[0] * (9/5))+32)


#create data frame

data_dict = {
    "students": ["Amy", "Bunny", "Caty"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print(data[data.students == "Amy"].scores[0])
data.to_csv("output.csv", index=False)


squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = squirrel['Primary Fur Color'].dropna()
fur = fur_colors.unique()
fur_count = []
for f in fur:
    fur_count.append(fur_colors[fur_colors == f].count())

fur_dict = {
    "Fur Color": fur,
    "Count": fur_count
}

fur_data = pd.DataFrame(fur_dict)
fur_data.to_csv("fur_count.csv", index=False)
