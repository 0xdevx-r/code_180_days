'''
Return a list containing the names of students whose course is "Python"
    Use .items()
    Use a for loop
    Do not modify students
    Do not print inside the function'''

#creating students dictionary

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

#defining a function with students parameter

def get_student_course(students):
    student_list = []

    for key,value in students.items():
        if value['course'] == "Python":
            student_list.append(value["name"])
    return student_list

print(get_student_course(students))
