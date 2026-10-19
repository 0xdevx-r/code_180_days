# Write a function that returns the student name with the highest total marks.

'''Requirements:

Use .items()
Use a for loop
Calculate total marks with a loop
Do not use sum()
Do not use max()
Do not use sorted()
Do not modify students
Do not print inside the function'''

students = {
    "S101": {"name": "Aarav", "marks": [78, 85, 92]},
    "S102": {"name": "Maya", "marks": [45, 55, 60]},
    "S103": {"name": "Rohan", "marks": [88, 91, 84]},
    "S104": {"name": "Neha", "marks": [35, 40, 50]},
    "S105": {"name": "Kabir", "marks": [70, 65, 75]}
}

def get_topper(students):
    highest_mark = float("-inf")
    topper = ''
    for key,value in students.items():
        total_marks = 0
        
        for mark in value['marks']:
            total_marks += mark
        if total_marks > highest_mark:
            highest_mark = total_marks
            topper = value['name']
    return topper

print(get_topper(students))