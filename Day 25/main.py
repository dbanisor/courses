# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.day)

### Get data in columns
# print(data["condition"])
# print(data.condition)

### Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# fahrenheit = int(monday.temp) * 2 + 30
# print(fahrenheit)

### Create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 46, 56]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
#
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
colors_table = pandas.DataFrame(data_dict)

colors_table.to_csv("squirrel_count.csv")