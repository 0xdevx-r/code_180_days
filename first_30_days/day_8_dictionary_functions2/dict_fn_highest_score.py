
''' Return the highest score, not the student's name.
    Use a for loop.
    Use .items().
    Do not use max().
    Do not sort.
    Do not modify scores.
    Do not print inside the function. '''

scores = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}

def get_highest_score(scores):
    highest_score = 0
    for name, score in scores.items():
        if score > highest_score:
            highest_score = score
    return highest_score

print(get_highest_score(scores))