import json

new_data = {
    "some_json_data": {
    "email": "poiuytre@email.com",
    "phone": "098765432"
    }
}

other_data = {
    "email": "aaaaaaa@email.com",
    "phone": "55555"
}

''' dump() is the JSON method for writing to a file. 
dump() serializes data by creating JSON data from a Python dictionary '''

# with open("example_files/some_json_file.json", "w") as data_file:
#     json.dump(new_data, data_file, indent=4)      ### the "indent=4" helps make the file easier to read by indenting all the JSON data ###

''' load() deserializes data by Python dictionaries from JSON data '''

# with open("example_files/some_json_file.json", "r") as data_file:
#     data = json.load(data_file)
#     print(data)

''' update() updates by adding to the JSON data '''

with open("example_files/some_json_file.json", "r") as data_file:
    # Reading the old data
    data = json.load(data_file)
    # Updating old data with new data
    data.update(other_data)

with open("example_files/some_json_file.json", "w") as data_file:
    # Saving the updated data
    json.dump(data, data_file, indent=4)