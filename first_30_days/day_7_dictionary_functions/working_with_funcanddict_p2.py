"""Add "department" to the dictionary.
Its value must come from the department parameter.
Return the updated dictionary.
Don't create a new dictionary.
Don't print inside the function."""

# Given a dictionary

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Junior Developer"
}

def add_department(employee, department):
    employee["department"] = department
    return employee

print(add_department(employee,"Engineering"))