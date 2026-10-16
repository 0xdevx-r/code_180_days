'''
Requirements:

    Return names of students whose course is "Python" AND age is 22 or above
    Use .items()
    Use one for loop
    Do not modify students
    Do not print inside the function

    Expected result:'''
# Return names of students whose course is "Python" AND age is 22 or above
# creating a sample dictionary

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

def get_student_details(students):
    student_list = []

    for key, value in students.items():
        if value['course'] == "Python" and value['age'] >= 22:
            student_list.append(value['name'])
    return student_list

print(get_student_details(students))
