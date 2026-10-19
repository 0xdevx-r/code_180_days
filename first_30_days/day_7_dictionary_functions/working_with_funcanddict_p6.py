""" Requirements:

    Return the name of the student with the highest score.
    Use a for loop.
    Use .items().
    Do not use max().
    Do not sort the dictionary.
    Return only the student's name, not a list.
    Do not print inside the function. """

# creating the dictionary

scores = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}

# creating the funcion to return topper student name

def topper_student(scores):
    highest_score = 0
    topper = ""
    for name, score in scores.items():
        if score > highest_score:
            highest_score = score
            topper = name
    return topper

print(topper_student(scores))