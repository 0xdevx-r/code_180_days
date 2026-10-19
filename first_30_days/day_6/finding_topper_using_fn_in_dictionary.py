# creating a function for finding the student name with highest marks in a dictionary

scores = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}
def max_marks_student(scores):
    topper_student = []
    highest_marks = 0
    for name, score in scores.items():
        if score > highest_marks:
            highest_marks = score
            topper_student = [name]
        elif score == highest_marks:
            topper_student.append(name)
    return topper_student

print(max_marks_student(scores))
