
# update the nested data:  change 'age' to 23 & 'city' to 'Jaipur'

student = {
    "name": "Alex",
    "details": {
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
}

student["details"]["age"] = 23
student["details"]["city"] = "Jaipur"

print(student['details']['age'])
print(student["details"]["city"])

#version 2

student = {
    "name": "Alex",
    "details": {
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
}

student["details"].update({"age": 23})
student["details"].update({"city":"Jaipur"})
print(student["details"]["age"])
print(student["details"]["city"])