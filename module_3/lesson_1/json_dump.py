#! /usr/bin/env python3
"""
A script which creates dictionaries representing
customers, employees and their skills, and products
and outputs them to a JSON (JavaScript Object Notation) file.
"""
import json


def main():
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

    data_model = {
        'customerEmail': cust_emails,
        'employeeSkills': employee_skills,
        'numProducts': num_products,
        'emailOrders': email_orders
    }

    # Get JSON string.  Indent option makes it more readable.  
    json_data = json.dumps(data_model, indent=4)

    print(json_data)

    with open('output_data_model.json', mode='w') as f:
        f.write(json_data)


if __name__ == '__main__':
    main()
