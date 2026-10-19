''' Return:

"gmail_users" → names of employees whose email ends with gmail.com
"skill_counts" → dictionary mapping employee ID → number of skills
"python_developers" → names of employees whose skills contain "Python"
"email_digit_counts" → dictionary mapping employee ID → number of digits in their email

Requirements
Use .items()
Use .split() for skills
Use loops
Manually count skills and digits
No count()
No list comprehensions
No previous functions
Do not modify employees
No print() inside the function
Return exactly the 4 required keys'''

employees = {
    "E101": {
        "name": "Aarav",
        "email": "aarav123@gmail.com",
        "skills": "Python, SQL, Git"
    },
    "E102": {
        "name": "Maya",
        "email": "maya45@yahoo.com",
        "skills": "Excel, SQL"
    },
    "E103": {
        "name": "Rohan",
        "email": "rohan.dev@gmail.com",
        "skills": "Python, FastAPI, SQL"
    },
    "E104": {
        "name": "Neha",
        "email": "neha99@outlook.com",
        "skills": "Python, Git"
    },
    "E105": {
        "name": "Kabir",
        "email": "kabir.dev@gmail.com",
        "skills": "Java, SQL, Git"
    }
}

def get_emp_detail(employees):
    gmail_users = []
    skill_counts = {}
    python_developers = []
    email_digit_counts = {}

    for key,value in employees.items():
        if 'Python' in value['skills'].split(', '):
            python_developers.append(value['name'])

        skill_count = 0
        for skill in value['skills'].split(', '):
            skill_count += 1
        skill_counts[key] = skill_count

        if value['email'].split('@') [1] == 'gmail.com':
            gmail_users.append(value['name'])

        email_digit = 0
        for char in value['email']:
            if char.isnumeric():
                email_digit += 1
        email_digit_counts[key] = email_digit
    return {

        "gmail_users": gmail_users,
        "skill_counts": skill_counts,
        "python_developers": python_developers,
        "email_digit_counts": email_digit_counts
        
        }

print(get_emp_detail(employees))