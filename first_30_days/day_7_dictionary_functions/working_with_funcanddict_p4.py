""" Requirements:

    Return True if the employee's role is "Senior Developer".
    Otherwise return False.
    Do not print inside the function.
    Do not use if/else for this one. """

# creating a dictionary

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Senior Developer"
}

# creating a function to check if employee's role is "Senior Developer"

def check_emp_role(employee):
    return employee['role'] == 'Senior Developer'

print(check_emp_role(employee))