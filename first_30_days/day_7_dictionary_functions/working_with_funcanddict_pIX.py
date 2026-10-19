''' Return a dictionary containing:

    "passed" → list of students with marks >= 50
    "failed" → list of students with marks < 50
    "topper" → name of the student with the highest marks'''

# creating a dictionary of students with name and marks

students = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}

# creating a dictionary with outlined engineering guidelines

def get_student_dictionary(students, marks):
    highest_score = 0
    passed = []
    failed = []
    topper = ""
    student_dictionary = {}

    for name, score in students.items():
        if score >= marks:
            passed.append(name)
        else:
            failed.append(name)

# for toppers

        if score > highest_score:
            highest_score = score
            topper = name
    student_dictionary.update({'passed' : passed})
    student_dictionary.update({'failed' : failed})
    student_dictionary.update({'topper' : topper})
    return student_dictionary

print(get_student_dictionary(students,50))