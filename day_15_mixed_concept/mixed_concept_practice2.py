''' Return:
"gmail_users" → list of student names whose email ends with "@gmail.com"
"digit_counts" → dictionary mapping each student ID to the number of digits in their email
Requirements:
- Use .items()
- Use loops and manual counting for digits
- Use string methods where appropriate
- No count()
- No list comprehensions
- No previous functions
- Do not modify students
- No print() inside the function
'''
students = {
    "S101": {"name": "Aarav", "email": "aarav123@gmail.com"},
    "S102": {"name": "Maya", "email": "maya45@yahoo.com"},
    "S103": {"name": "Rohan", "email": "rohan.dev@gmail.com"},
    "S104": {"name": "Neha", "email": "neha99@outlook.com"},
    "S105": {"name": "Kabir", "email": "kabir.dev@gmail.com"}
}

def get_student_detail(students):
    gmail_users = []
    digit_count ={}

    for key,value in students.items():
        email_domain = '@' + value['email'].split('@')[1]
        if email_domain == '@gmail.com':
            gmail_users.append(value['name'])

        num_count  = 0
        for char in value['email']:
            if char.isnumeric():
                num_count += 1

        digit_count[key] = num_count
        
    return {

        "gmail_users" : gmail_users,
        "digit_counts" : digit_count
    }

print(get_student_detail(students))
