'''Return a list of student names whose average marks are greater than or equal to passing_average.
    Calculate each average using a loop.
    Use .items() to iterate through the dictionary.
    Do not use sum(), len(), or sorted().
    Do not use list comprehensions.
    Do not modify students.
    Do not print inside the function.'''

students = {
    "S101": {"name": "Aarav", "marks": [78, 85, 92]},
    "S102": {"name": "Maya", "marks": [45, 55, 60]},
    "S103": {"name": "Rohan", "marks": [88, 91, 84]},
    "S104": {"name": "Neha", "marks": [35, 40, 50]},
    "S105": {"name": "Kabir", "marks": [70, 65, 75]}
}

def get_students_details(students, passing_average):
    above_average_students = []

    for key, value in students.items():
        score_count = 0
        total_marks = 0

        for mark in value['marks']:
            score_count += 1
            total_marks += mark

        avg_mark = total_marks/score_count

        if avg_mark >= passing_average:
            above_average_students.append(value['name'])

    return above_average_students

print(get_students_details(students, 60))