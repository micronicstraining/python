#! /usr/bin/env python3
# Create a pickle_data.py script which
# takes the data_model variable from lesson_1 in the json_dump.py script
# and pickles that object into a pickle FILE_NAME

# Then load and deserailizes this file and show the data
# Print out a specific key-value pair
import pickle

# replace data with data_model variable
# Customer name and e-mail address
cust_emails = {
    'John Doe': 'johndoe@gmail.com',
    'Sally Sue': 's.sue@yahoo.com',
    'Richard Smith': 'richard.smith@bing.com'
}

# Employee name to skills
employee_skills = {
    'John Doe': ['Networking', 'Programming', 'Project Management'],
    'Sally Sue': ['CTO', 'Security', 'DevOps']
}

# Product type and number available
num_products = {
    'tv': 100,
    'computer': 50,
    'watch': 30
}

# Email to product orders
email_orders = {
    'johndoe@gmail.com': {'tv': 1, 'watch': 2},
    'richard.smith@bing.com': {'computer': 10}
}

assert email_orders['johndoe@gmail.com']['tv'] == 1

data = {
    'customerEmail': cust_emails,
    'employeeSkills': employee_skills,
    'numProducts': num_products,
    'emailOrders': email_orders
}

FILE_NAME = 'lesson2.lab1.pickle'

# Serialize the data using pickle binary format
with open(FILE_NAME, mode="wb") as f:
    pickle.dump(data, f)

input('')

# Deserialize (unpickle) data from file
unpickled_data = None
with open(FILE_NAME, mode="rb") as f:
    unpickled_data = pickle.load(f)

# print(unpickled_data)
if 'customerEmail' in unpickled_data:
    print(data['customerEmail'].keys())

# for example the following should work
# print(data['customerEmail'].keys())
