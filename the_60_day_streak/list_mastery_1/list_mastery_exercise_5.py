''' 
RETURN:

"averages" → dictionary mapping each student's name → their average mark.
"passed_students" → students whose average is at least 60, preserving original order.
"top_student" → name of the student with the highest average.
"highest_mark" → highest individual mark across all students.

Restrictions:

Use loops.
Manually calculate sums and counts.
No sum()
No len()
No max()
No sorted()
No list comprehensions.
Do not modify students.
No print() inside the function.
Return exactly the four required keys.'''

students = [
    {"name": "Aarav", "marks": [78, 85, 92]},
    {"name": "Maya", "marks": [65, 72, 68]},
    {"name": "Rohan", "marks": [90, 88, 95]},
    {"name": "Neha", "marks": [55, 61, 58]},
    {"name": "Kabir", "marks": [82, 79, 85]}
]

def get_students_detaisl(students):
    averages = {}
    passed_students = []
    top_student = ''
    highest_mark = float('-inf')
    highest_average = float('-inf')

    for student_details in students:
        total_marks = 0
        sub_count = 0
       
        
        for mark in student_details['marks']:
            total_marks += mark
            sub_count += 1
            
            if mark > highest_mark: 
                highest_mark = mark

        average_marks = total_marks/sub_count
        averages[student_details['name']] = average_marks

        if average_marks >= 60:
            passed_students.append(student_details['name'])

        if average_marks > highest_average:
            highest_average = average_marks
            top_student = student_details['name']

    return {'averages':averages, 'passed_students': passed_students, 'highest_mark': highest_mark, 'top_student': top_student}

print(get_students_detaisl(students))