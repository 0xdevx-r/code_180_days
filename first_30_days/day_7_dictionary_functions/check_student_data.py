# Function checks dictionary data
# check if student's age is above 18


def check_student_data():
    student = {"name":"Alex", "age": 22, "course":"Python"}
    return student['age'] >= 18

print(check_student_data())