'''Write a function that returns a dictionary containing:
    "passed" → names of students whose average marks are >= passing_average
    "failed" → names of students whose average marks are < passing_average
    "topper" → name of the student with the highest average marks
    Test with passing_average = 60.
    Requirements:
    Use .items()
    Use one outer for loop; an inner loop for marks is allowed.
    Calculate averages manually.
    Do not use sum(), len(), max(), or sorted().
    Do not use list comprehensions.
    Do not call your previous functions.
    Do not modify students.
    Do not print inside the function.
    Return exactly the three required keys.'''

students = {
    "S101": {"name": "Aarav", "marks": [78, 85, 92]},
    "S102": {"name": "Maya", "marks": [45, 55, 60]},
    "S103": {"name": "Rohan", "marks": [88, 91, 84]},
    "S104": {"name": "Neha", "marks": [35, 40, 50]},
    "S105": {"name": "Kabir", "marks": [70, 65, 75]}
}

def get_student_data(students, passing_average):
    passed = []
    failed = []
    topper = ''
    highest_mark  = float('-inf')

    for key,value in students.items():
        total_marks = 0
        count = 0

        for mark in value['marks']:
            total_marks += mark
            count += 1
        average = total_marks/ count
        if average > highest_mark:
            highest_mark = average
            topper = value['name']
    
        if average >= passing_average:
            passed.append(value['name'])

        else:
            failed.append(value['name'])

    return {
        "passed": passed,
        "failed": failed,
        "topper": topper 
    }

print(get_student_data(students, 60))