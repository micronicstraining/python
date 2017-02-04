#! /usr/bin/env python3
# Create a pickle_data.py script which
# takes the data_model variable from lesson_1 in the json_dump.py script
# and pickles that object into a pickle FILE_NAME

# Then load and deserailizes this file and show the data
# Print out a specific key-value pair
import pickle


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

data_model = {
    'customerEmail': cust_emails,
    'employeeSkills': employee_skills,
    'numProducts': num_products,
    'emailOrders': email_orders
}

file_name = 'lesson2.lab1.pickle'
with open(file_name, mode="wb") as f:
    pickle.dump(data_model, f)


with open(file_name, mode="rb") as f:
    data = pickle.load(f)
    print(data)
    print(data['customerEmail'].keys())
