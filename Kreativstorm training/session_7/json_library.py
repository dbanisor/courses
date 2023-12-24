import json

a = {"name": "John",
     "age": 31,
     "Salary": 25000}
#----------------------------------------------------------------------------------------------------------------------#
#outputing to the console

# b = json.dumps(a, indent=2)       # dumps creates a json object from that dictionary

    # DUMPS puts the output in the console, as a string
    # DUMP puts the output in a file

# print(b)
#----------------------------------------------------------------------------------------------------------------------#
#outputing to a file
# with open('sample.json', 'w') as p:
#     json.dump(a, p, indent=2)

#----------------------------------------------------------------------------------------------------------------------#
#inputing a json object from a string, not from a file ----> LOADS

# employee = '{"id": "09", "name":"Bob", "department":"Finance"}'
#
# employee_dict = json.loads(employee)
# print(employee_dict)

#----------------------------------------------------------------------------------------------------------------------#
#inputing a json object from file, not from a string ----> LOAD

# with open("sample.json", "r") as f:
#     print(json.load(f))


# json_data = '{"name": "John", "age": 30, "city": "New York"}'
#
# data = json.loads(json_data)
#
# print("Name:", data["name"])
# print("Age:", data["age"])
# print("City:", data["city"])

'''1. Create a JSON structure that includes nested objects, such as information about a company with departments and 
employees. Parse the JSON and retrieve specific employee details.
'''
company_data = '''{
    "company_name": "Acme Corporation",
    "departments": [
        {
            "name": "HR",
            "employees": [
                {"name": "Alice", "salary": 60000},
                {"name": "Bob", "salary": 55000}
            ]
        },
        {
            "name": "Engineering",
            "employees": [
                {"name": "Charlie", "salary": 80000},
                {"name": "David", "salary": 75000}
            ]
        }
    ]
}
'''
# data = json.loads(company_data)

# dept = data['departments'][1]['employees']
# name1 = dept[0]['name']
# salary1 = dept[0]['salary']
#
# name2 = dept[1]['name']
# salary2 = dept[1]['salary']
#
# print(f"Name: {name1}, Salary: {salary1}")
# print(f"Name: {name2}, Salary: {salary2}")

#____________________________ or ___________________________#
# for dept in data["departments"]:
#     if dept["name"] == "Engineering":
#         print(f"Engineering Department: {dept['employees']}")

'''Filter products with prices between $10 and $50 and sort by name.'''

with open('products.json', 'r') as f:
     data = json.load(f)


products = []

for product in data:
     if product['price'] > 10 and product['price'] < 50:
          products.append(product)

print(sorted(products, key=lambda x: x['name']))
