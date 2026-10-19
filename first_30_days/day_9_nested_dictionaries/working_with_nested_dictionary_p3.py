# working with nested dictionary and function

# write a function which accepts the student dictionary
# return the student's course
# do not print

# creating the dictionary

student = {
    "name": "Alex",
    "details": {
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
}

def get_student_course(student):
    return student['details']['course']

print(get_student_course(student))