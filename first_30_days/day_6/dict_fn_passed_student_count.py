# finding number of students passed in dictionary of students
# Inside the function checking the score using loop

scores = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}

def passed_students(scores):
    
    students = []
    for name, score in scores.items():
        if score >= 50:
            students.append(name)
    return students

print(passed_students(scores))