'''Requirements:

    Return a list of employee names
    Include employees whose salary is greater than salary_limit
    Use .items()
    Use a for loop
    Access the nested "name" and "salary" values
    Do not use sorted()
    Do not modify employees
    Do not print inside the function'''


employees = {
    "E101": {"name": "Aarav", "salary": 45000, "department": "IT"},
    "E102": {"name": "Maya", "salary": 62000, "department": "HR"},
    "E103": {"name": "Rohan", "salary": 55000, "department": "IT"},
    "E104": {"name": "Neha", "salary": 70000, "department": "Finance"},
    "E105": {"name": "Kabir", "salary": 48000, "department": "IT"}
}

# defining the function

def get_high_earners(employees, salary_limit):
    high_earners = []

    for key, value in employees.items():
        if value['salary'] > salary_limit:
            high_earners.append(value['name'])
    return high_earners

print(get_high_earners(employees, 50000))