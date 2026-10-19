'''Requirements

    Return a dictionary containing:

    "matching_students" → names whose course matches course AND age is >= min_age
    "count" → number of matching students
    "youngest" → name of the youngest matching student
    Constraints
    Use .items()
    Use one for loop
    Do not modify students
    Do not use min(), max(), or sorted()
    Do not use previous functions
    Do not use len() for "count"
    Do not print inside the function
    Use the course and min_age parameters
    Follow the exact output keys'''

# students dictionary

students = {
    "s1": {
        "name": "Aarav",
        "course": "Python",
        "age": 23
    },
    "s2": {
        "name": "Maya",
        "course": "Java",
        "age": 25
    },
    "s3": {
        "name": "Rohan",
        "course": "Python",
        "age": 20
    },
    "s4": {
        "name": "Neha",
        "course": "Python",
        "age": 27
    },
    "s5": {
        "name": "Kabir",
        "course": "Java",
        "age": 22
    }
}

def analyze_students(students, course, min_age):
    matching_students = []
    count = 0
    youngest = float("inf")
    youngest_student_name = None
    for key, value in students.items():
        if value['course'] == course and value['age'] >= min_age:
            matching_students.append(value['name'])
            count += 1
            if value['age']< youngest:
                youngest = value['age']
                youngest_student_name = value['name']

    return {
        "matching_students" : matching_students,
        "count" : count,
        "youngest" : youngest_student_name
    }

print(analyze_students(students, "Python", 21))