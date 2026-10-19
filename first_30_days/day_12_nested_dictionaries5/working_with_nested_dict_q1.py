'''Requirements:

    Return a list of employee names
    Include only employees whose department equals department
    Use .items()
    Use a for loop
    Access the nested "name" and "department" values
    Do not use list comprehension
    Do not modify employees
    Do not print inside the function'''


employees = {
    "E101": {"name": "Aarav", "salary": 45000, "department": "IT"},
    "E102": {"name": "Maya", "salary": 62000, "department": "HR"},
    "E103": {"name": "Rohan", "salary": 55000, "department": "IT"},
    "E104": {"name": "Neha", "salary": 70000, "department": "Finance"},
    "E105": {"name": "Kabir", "salary": 48000, "department": "IT"}
}

def get_department_employees(employees, department):
    employee_names = []
    
    for key, value in employees.items():
        if value['department'] == department:
            employee_names.append(value['name'])
    return employee_names

print(get_department_employees(employees, "IT"))