""" Requirements:

    Return a list of employee names whose salary is greater than or equal to minimum_salary.
    Use .items().
    Use a for loop.
    Use the minimum_salary parameter.
    Do not modify the dictionary.
    Do not use filter(), max(), sorted(), etc."""

# creating a dictionary of employees with respective salary

employees = {
    "Alex": 72000,
    "John": 45000,
    "Mike": 68000,
    "Sara": 91000,
    "Tom": 52000
}

# creating a function to get the name of employee whose salary is greater or equal to mininum_salary
# defining minimum_salary within function

def get_emp_names(employees, min_salary):
    employee_name_list = []
    for name, salary in employees.items():
        if salary >= min_salary:
            employee_name_list.append(name)
    return employee_name_list

print(get_emp_names(employees, 70000))