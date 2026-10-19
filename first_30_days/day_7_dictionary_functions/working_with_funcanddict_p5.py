""" Requirements:

    Return a list containing the names of students who scored below 50.
    Use a for loop.
    Use .items().
    Do not modify scores.
    Do not print inside the function. """

#   creating a dictionary

scores = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}

# creating a function
def get_failed_students(scores):
    failed_students = []
    for name, score in scores.items():
        if score < 50:
            failed_students.append(name)
    return failed_students

print(get_failed_students(scores))