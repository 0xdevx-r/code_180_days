'''
Return:

department_employees → Department → list of employee names, original order
skill_counts → Skill → number of employees having that skill
python_developers → employees whose skills contain "Python", original order
department_counts → Department → number of employees
unique_skills → all unique skills, preserving first-seen order.

Restrictions: No len(), count(), sum(), max(), min(), sorted(), set(), or comprehensions.
No mutation of employees; no print() inside the function.'''

employees = [
    {"name": "Aarav", "department": "Backend", "skills": ["Python", "SQL", "Git"]},
    {"name": "Maya", "department": "Frontend", "skills": ["HTML", "CSS", "JavaScript"]},
    {"name": "Rohan", "department": "Backend", "skills": ["Python", "Docker"]},
    {"name": "Neha", "department": "Data", "skills": ["Python", "SQL", "Pandas"]},
    {"name": "Kabir", "department": "Backend", "skills": ["Python", "SQL", "Git"]},
    {"name": "Ishaan", "department": "Data", "skills": ["Python", "Pandas", "SQL"]}
]

def get_emp_data(employees):
    department_employees = {}
    skill_counts = {}
    python_developers = []
    department_counts = {}
    unique_skills = []

    for employee in employees:

        if employee['department'] not in department_employees:
            department_employees[employee['department']] = [employee['name']]
        else:
            department_employees[employee['department']].append(employee['name'])

        for skill in employee['skills']:

            if skill not in skill_counts:
                skill_counts[skill] = 1
            else:
                skill_counts[skill] += 1
            if skill == 'Python' and employee['name'] not in python_developers:
                python_developers.append(employee['name'])

            if skill not in unique_skills:
                unique_skills.append(skill)

        if employee['department'] not in department_counts:
            department_counts[employee['department']] = 1

        else:
            department_counts[employee['department']] += 1


    return {
        'department_employees': department_employees,
        'skill_counts': skill_counts,
        'python_developers': python_developers,
        'department_counts': department_counts,
        'unique_skills': unique_skills
    }

print(get_emp_data(employees))