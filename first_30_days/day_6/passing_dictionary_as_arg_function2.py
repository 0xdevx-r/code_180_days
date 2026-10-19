
# passing a dictionary into a function an an argument

def get_student_name(student):
    return student['name']

student = {"name":"Alex","age": 22, "course":"Python"}

print(f"{get_student_name(student)}")