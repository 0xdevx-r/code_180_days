''' Requirements:
    Return below data as dictionary-

    high_earners → names of employees whose salary is greater than salary_limit
    count → number of high earners
    highest_paid → name of employee with the highest salary
    Use .items()
    Use one for loop
    Do not use max(), sorted(), or len()
    Do not call previous functions
    Do not modify employees
    Do not print inside the function
    Exact dictionary keys matter'''

# dictionary 

employees = {
    "E101": {"name": "Aarav", "salary": 45000, "department": "IT"},
    "E102": {"name": "Maya", "salary": 62000, "department": "HR"},
    "E103": {"name": "Rohan", "salary": 55000, "department": "IT"},
    "E104": {"name": "Neha", "salary": 70000, "department": "Finance"},
    "E105": {"name": "Kabir", "salary": 48000, "department": "IT"}
}

def get_emp_data(employees, salary_limit):
    high_earners = []
    count = 0
    highest_paid_salary = float("-inf")
    highest_paid = ""

    for key,value in employees.items():
        if value['salary'] > salary_limit:
            high_earners.append(value['name'])
            count += 1
        if value['salary'] >  highest_paid_salary:
            highest_paid_salary = value['salary']
            highest_paid = value['name']

    return {
        "high_earners": high_earners,
        "count": count,
        "highest_paid": highest_paid
    }

print(get_emp_data(employees,50000))