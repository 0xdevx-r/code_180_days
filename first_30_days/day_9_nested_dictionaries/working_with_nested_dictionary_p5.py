# write a function which returns a list containing names of the students whose course is "Python"
# do not print inside the function


students = {
    "student1": {
        "name": "Alex",
        "course": "Python",
        "age": 22
    },
    "student2": {
        "name": "Sam",
        "course": "Java",
        "age": 24
    },
    "student3": {
        "name": "John",
        "course": "Python",
        "age": 21
    }
}

def get_python_students(students):
    student_list = []
    for student in students.values():
        if student['course'] == "Python":
            student_list.append(student["name"])
    return student_list

print(get_python_students(students))