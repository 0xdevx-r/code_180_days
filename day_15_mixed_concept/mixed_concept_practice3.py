''' RETURN

"python_developers" → names of employees whose skills contain "Python"
"skill_counts" → dictionary mapping each employee ID to the number of skills they have
"sql_users" → names of employees whose skills contain "SQL"

REQUIREMENTS:
Use .items()
Use string methods such as .split()
Use loops
Manually determine the skill count
No count()
No list comprehensions
No previous functions
Do not modify employees
No print() inside the function
Return exactly the three required keys.
'''

employees = {
    "E101": {"name": "Aarav", "skills": "Python, SQL, Git"},
    "E102": {"name": "Maya", "skills": "Excel, SQL"},
    "E103": {"name": "Rohan", "skills": "Python, FastAPI, SQL"},
    "E104": {"name": "Neha", "skills": "Python, Git"},
    "E105": {"name": "Kabir", "skills": "Java, SQL, Git"}
}

def get_emp_details(employees):
    python_developers = []
    skill_counts = {}
    sql_users = []

    for e_id, details in employees.items():
        total_skill = 0
        emp_skill = details['skills'].split(",")

        if 'Python' in emp_skill:
            python_developers.append(details['name'])

        if 'SQL' in details['skills']:
            sql_users.append(details['name'])
        
        for skill in emp_skill:
            total_skill += 1
        skill_counts[e_id] = total_skill
    
    return {

        'python_developers' : python_developers,
        'skill_counts': skill_counts,
        'sql_users': sql_users
    }

print(get_emp_details(employees))