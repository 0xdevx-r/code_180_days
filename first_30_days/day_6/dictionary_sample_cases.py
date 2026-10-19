# test files for dictionaries
# fetching value of name from dictionary
student = {
    "name": "Alex",
    "age": 22,
    "course": "Python"
}

print(f"{student['name']}")

# fetching all the key, value from created dictionary

student = {
    "name": "Alex",
    "age": 22,
    "course": "Python"
}

for key, value in student.items():
    print(f"{key}, {value}")

# Modify the dictionary by adding: "city": "Delhi", "age": 22
# change age to 23

student = {
    "name":"Alex",
    "age": 22,
    "course": "Python",
    "city":"Delhi"
}
print(f"{student['city']}")
student.update({"age": 23})
print(f"{student['age']}")
