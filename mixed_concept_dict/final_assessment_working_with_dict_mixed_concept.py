'''
"gmail_users"- List employee names whose email ends with "gmail.com".
"name_lengths"-Dictionary mapping employee ID → number of characters in their name.
Manually count characters using a loop.

"skill_counts"
Dictionary mapping employee ID → number of skills.
Skills are comma-separated.

"python_developers"
List employee names whose skills contain "Python".

"email_digit_counts"
Dictionary mapping employee ID → number of digits in their email.
Manually count using a loop.

Restrictions
Must use .items()
Must use loops
Must use .endswith()
No count()
No list comprehensions
No len()
No max(), sorted(), filter(), etc.
No previous functions
Do not modify employees
No print() inside the function
Return exactly the 5 required keys'''

employees = {
    "E101": {
        "name": "Aarav",
        "email": "aarav123@gmail.com",
        "skills": "Python, SQL, Git"
    },
    "E102": {
        "name": "Maya",
        "email": "maya45@yahoo.com",
        "skills": "Python, Django"
    },
    "E103": {
        "name": "Rohan",
        "email": "rohan.dev@gmail.com",
        "skills": "Java, SQL, Docker"
    },
    "E104": {
        "name": "Neha",
        "email": "neha99@gmail.com",
        "skills": "Python, FastAPI"
    },
    "E105": {
        "name": "Kabir",
        "email": "kabir.dev@outlook.com",
        "skills": "Python, SQL, Git"
    }
}

def get_emp_details(employees):
    gmail_users = []
    name_lengths = {}
    skill_counts = {}
    python_developers = []
    email_digit_counts = {}

    for key,value in employees.items():
        if value['email'].endswith('@gmail.com'):
            gmail_users.append(value['name'])

        char_count = 0
        for char in value['name']:
            char_count += 1
        name_lengths[key] = char_count

        skills = 0
        for skill in value['skills'].split(', '):
            skills += 1
        skill_counts[key] = skills

        if 'Python' in value['skills']:
            python_developers.append(value['name'])

        digit_count = 0
        for digit in value['email']:
            if digit.isnumeric():
                digit_count += 1
        email_digit_counts[key] = digit_count

    return {

        'gmail_users': gmail_users,
        'name_lengths': name_lengths,
        'skill_counts': skill_counts,
        'python_developers': python_developers,
        'email_digit_counts': email_digit_counts

    }

print(get_emp_details(employees))