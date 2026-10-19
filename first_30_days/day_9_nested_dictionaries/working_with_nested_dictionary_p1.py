# writing code to access the data from the nested dictionary

student = {
    "name": "Alex",
    "details": {
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
}

print(student['name'])
print(student['details']['course'])
print(student['details']['city'])