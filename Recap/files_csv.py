""" OPENING A FILE AND READING FROM IT USING IMPORT CSV """

import csv

with open("example_files/csv_example.csv") as file:
    content = csv.reader(file)
    temperatures = []
    print(temperatures)
    for row in content:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        print(row)

print(temperatures)

""" OPENING A FILE AND READING FROM IT USING IMPORT PANDAS """

import pandas

data = pandas.read_csv("example_files/csv_example.csv")
print(data)

""" TURNING DATA INTO A DICTIONNARY WITH PANDAS """

data_dict = data.to_dict()
print(data_dict)

""" TURNING A COLUMN INTO A LIST WITH PANDAS """

temp_list = data["temp"].to_list()
print(temp_list)

""" GET DATA IN COLUMNS WITH PANDAS """
print(data.day)

""" GET DATA IN ROWS WITH PANDAS """

print(data[data.day == "Monday"])
