''' RETURN:
"gmail_users" → names of students whose email ends with @gmail.com
"email_digit_counts" → dictionary mapping each student ID to the number of digits in their email
"name_lengths" → dictionary mapping each student ID to the length of their name

REQUIREMENTS:
Use .items() and loops.
Manually count digits and name characters.
No count(), no list comprehensions, no previous functions.
Do not modify students.
No print() inside the function.
Return exactly the 3 required keys.'''


students = {
    "S101": {"name": "Aarav", "email": "aarav123@gmail.com"},
    "S102": {"name": "Maya", "email": "maya45@yahoo.com"},
    "S103": {"name": "Rohan", "email": "rohan.dev@gmail.com"},
    "S104": {"name": "Neha", "email": "neha99@outlook.com"},
    "S105": {"name": "Kabir", "email": "kabir.dev@gmail.com"}
}

def get_student_data(students):
    gmail_users = []
    email_digit_counts = {}
    name_lengths = {}

    for key,value in students.items():
        if value['email'].split('@')[1] == 'gmail.com':
            gmail_users.append(value['name'])

        digit_count = 0
        for char in value['email']:
            if char.isnumeric():
                digit_count += 1
            email_digit_counts[key] = digit_count

        name_char_count = 0
        for name_char in value['name']:
            name_char_count += 1
        name_lengths[key] = name_char_count

    return {

        "gmail_users": gmail_users,
        "email_digit_counts": email_digit_counts,
        "name_lengths": name_lengths
    }

print(get_student_data(students))