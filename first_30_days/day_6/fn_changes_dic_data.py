# function changes dictionary data and returns dictionary
# change age to 30

def get_student_data():
    student = {"name":"Alex", "age": 22}
    student['age'] = 30
    return student['age']

print(get_student_data())