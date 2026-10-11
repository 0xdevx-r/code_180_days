'''
Return a dictionary containing exactly:
 "employees" → names of employees in the given department
 "high_earners" → names of employees in that department whose salary is >= salary_limit
 "highest_paid" → name of the highest-paid employee in that department 
 
 Requirements:
- Use .items()
- One outer for loop
- No max(), sorted(), sum(), or list comprehensions
- Manually track the highest salary
- Do not modify employees
- Do not print inside the function
- Return exactly the three required keys'''

employees = {
    "E101": {"name": "Aarav", "department": "IT", "salary": 65000},
    "E102": {"name": "Maya", "department": "HR", "salary": 52000},
    "E103": {"name": "Rohan", "department": "IT", "salary": 78000},
    "E104": {"name": "Neha", "department": "Finance", "salary": 60000},
    "E105": {"name": "Kabir", "department": "IT", "salary": 55000}
}

def get_emp_details(employees,department,salary_limit):
    high_earners = []
    highest_salary = float("-inf")
    highest_paid = ''
    same_dept_employees = []

    for key,value in employees.items():
        
        if value['department'] == department and value['salary'] >= salary_limit:
            high_earners.append(value['name'])
        if value['salary'] > highest_salary and value['department'] == department:
            highest_salary = value['salary']
            highest_paid = value['name']
        if value['department'] == department:
            same_dept_employees.append(value['name'])

    return {
        
        "employees": same_dept_employees,
        "high_earners": high_earners,
        "highest_paid": highest_paid

    }

print(get_emp_details(employees, "IT", 60000))