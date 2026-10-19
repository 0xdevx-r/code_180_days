'''Requirements:

    Return the employee's name
    Find the employee with the highest salary
    Use .items()
    Use a for loop
    Do not use max()
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

def get_highest_paid_employee(employees):
    highest_paid = ""
    highest_salary = float("-inf")
    for key, value in employees.items():
        if value['salary'] > highest_salary:
            highest_salary = value['salary']
            highest_paid = value['name']
    return highest_paid

print(get_highest_paid_employee(employees))