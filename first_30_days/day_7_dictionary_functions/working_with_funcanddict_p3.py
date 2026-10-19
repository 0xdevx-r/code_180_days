""" Requirements:
    Return the employee's role.
    Do not modify the dictionary.
    Do not print inside the function."""

# creating a dictionary

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Software Engineer",
    "department": "Backend"
}

#   Reading the data through function

def find_emp_role(employee):
    return employee["role"]

print(find_emp_role(employee))