
# passing a dictionary into a function an an argument

def get_student_name():
        student = {
        "name":"Alex",
        "age": 22
        }
        return(f"{student['name']}")

print(get_student_name())