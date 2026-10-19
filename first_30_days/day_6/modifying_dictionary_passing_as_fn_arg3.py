# make the function modify dictionary data.
# update the age and return updated dictionary


student = {"name":"Alex", "age": 25}

def get_student_data(student):
    return student['age']

student.update({"age": 30})
print(get_student_data(student))