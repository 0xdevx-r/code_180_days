# update the nested data using function
# change the nested "city" to "new_city"
# return the modified dictionary
# do not create a new dictionary
# do not print inside the function

# creating the dictionary

student = {
    "name": "Alex",
    "details": {
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
}

def update_nested_data(student, new_city):
    student['details']['city'] = new_city
    return student

print(update_nested_data(student, "Mumbai"))