''' Write a function that returns:

    "passed": 
    "failed": 
    "topper":

    Rules:

    passed → students whose average >= 60
    failed → students whose average < 60
    topper → student with the highest total marks
    Use .items()
    Use one outer for loop
    You may use an inner loop for marks
    Calculate totals/averages manually
    Do not use sum(), len(), max(), or sorted()
    Do not call your previous functions
    Do not modify students
    Do not print inside the function
    Exact output keys matter'''


students = {
    "S101": {"name": "Aarav", "marks": [78, 85, 92]},
    "S102": {"name": "Maya", "marks": [45, 55, 60]},
    "S103": {"name": "Rohan", "marks": [88, 91, 84]},
    "S104": {"name": "Neha", "marks": [35, 40, 50]},
    "S105": {"name": "Kabir", "marks": [70, 65, 75]}
}

def get_student_results(students):
    highest_marks = float('-inf')
    topper = ''
    passed = []
    failed = []
    for key,value in students.items():
        mark_count = 0
        total_marks = 0
        for mark in value['marks']:
            total_marks += mark
            mark_count += 1

        average = total_marks/mark_count

        if average >= 60:
            passed.append(value['name'])

        else: 
            failed.append(value['name'])

        if total_marks > highest_marks:
            highest_marks = total_marks
            topper = value['name']
    return {
        "passed": passed, 
        "failed": failed,
        "topper": topper
    }

print(get_student_results(students))