'''
Return:
backend_employees
Names of employees in "Backend"
Preserve original order

skill_counts
Dictionary mapping employee name → number of skills
Count manually

python_developers
Names of employees whose skills contain "Python"
Preserve original order

unique_skills
Unique skills across all employees
Preserve first-appearance order

department_counts
Dictionary mapping department → number of employees

Restrictions
No:
len()
count()
sum()
set()
max()
sorted()
comprehensions
mutation of employees
print() inside the function'''

employees = [
    {
        "name": "Aarav",
        "department": "Backend",
        "skills": ["Python", "SQL", "Git"]
    },
    {
        "name": "Maya",
        "department": "Frontend",
        "skills": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "Rohan",
        "department": "Backend",
        "skills": ["Python", "Docker"]
    },
    {
        "name": "Neha",
        "department": "Data",
        "skills": ["Python", "SQL", "Pandas"]
    },
    {
        "name": "Kabir",
        "department": "Backend",
        "skills": ["Python", "SQL", "Git"]
    }
]

def get_emp_data(employees):
    backend_employees = []     # emp with 'Backend' as department
    skill_counts = {}          # emp name to num of skills
    python_developers = []     # emp name with Python as skill
    unique_skills = []         # unique skills across all emp skills
    department_counts = {}     # department to number of emp

    for employee in employees:
        total_skill = 0

        for skill in employee['skills']:
            total_skill += 1

            if skill not in unique_skills:
                unique_skills.append(skill)

        if employee['department'] == 'Backend':
            backend_employees.append(employee['name'])

        skill_counts[employee['name']] = total_skill

        if 'Python' in employee['skills']:
             python_developers.append(employee['name'])

        if employee['department'] not in department_counts:
            department_counts[employee['department']] = 1

        else:
            department_counts[employee['department']] += 1

    return {
        'backend_employees': backend_employees,
        'skill_counts': skill_counts,
        'python_developers': python_developers,
        'unique_skills': unique_skills,
        'department_counts' : department_counts
    }
            
print(get_emp_data(employees))