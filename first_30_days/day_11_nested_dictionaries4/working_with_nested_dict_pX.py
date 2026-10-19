''' Constraints
    Use .items()
    Use one for loop
    Do not modify students
    Do not use len() on the filtered list to calculate the count
    Do not use previous functions
    Do not print inside the function
    Follow the exact output keys'''

# creating the dictionary

students = {

    "student1": {"name": "Alex",
                "course": "Python",
                "age": 22},
    "student2": {"name": "Sam",
                "course": "Java",
                "age": 24},
    "student3": {"name": "John",
                 "course": "Python",
                 "age": 21},
    "student4": {"name": "Mike",
                 "course":"Python",
                 "age": 25}
    
}

'''defining a dictionary to return a dictionary containing:

"matching_students" → names whose course matches course AND age is >= min_age
"count" → number of matching students'''

def matching_students_data(students,min_age,matching_course):
    matching_students = []
    count = 0 
    for key,value in students.items():
        if value['age'] >= min_age and value['course'] == matching_course:
            matching_students.append(value["name"])
            count += 1
    return {
        "matching_students": matching_students,
        "count" : count
    }

print(matching_students_data(students, 22, 'Python'))