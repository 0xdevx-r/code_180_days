''' Requirements:

Return a list of student names whose age is 22 or above
Use .items()
Use a for loop
Do not modify students
Do not print inside the function'''

# Creating the dictionary
# Return a list of student names whose age is 22 or above

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

# creating a fucntion to return the list of students 

def get_student_list(students):
    student_list = []
    for key, value in students.items():
        if value['age'] >= 22:
            student_list.append(value['name'])
    return student_list

print(get_student_list(students))