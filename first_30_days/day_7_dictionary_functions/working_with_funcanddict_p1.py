# Update the employee's "role" to new_role.
# Return the updated dictionary.
# Do not create a new dictionary.
# Do not print inside the function.

# given dictionary employee

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Junior Developer"
}

# creating a function

def update_emp_role(employee, new_role):
    employee["role"] = new_role
    return employee

print(update_emp_role(employee, "Software Developer"))