'''Requirements:

    Find the student using student_id
    Change that student's "course" to new_course
    Modify the same students dictionary
    Return the modified dictionary
    Do not create a new dictionary
    Do not use a loop
    Do not print inside the function'''

# creating the nested dictionary

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

# defining the function for updating the data

def update_student_course(students, student_id, course):
    students[student_id]["course"] = course
    return students
print(update_student_course(students, "student3","Java"))
