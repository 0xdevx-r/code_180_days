'''
Return a dictionary containing:
1. student_totals — student ID → total marks, calculated manually.
2. averages — student name → average marks, calculated manually.
3. passed_students — names whose average is greater than or equal to 60, preserving original order.
4. top_student — name of the student with the highest average.
5. subject_highest_marks — highest individual mark found across all students.

Restrictions
No len(), sum(), max(), min(), sorted(), count(), set(), or comprehensions.

Also:
Don't mutate students.
Don't use print() inside the function.
Assume every student has at least one mark.
If two students tie for the highest average, return the first one.'''

students = [
    {"id": "S101", "name": "Aarav", "marks": [78, 85, 92]},
    {"id": "S102", "name": "Maya", "marks": [55, 62, 58]},
    {"id": "S103", "name": "Rohan", "marks": [90, 88, 95]},
    {"id": "S104", "name": "Neha", "marks": [65, 70, 72]},
    {"id": "S105", "name": "Kabir", "marks": [40, 45, 50]}
]

def get_student_details(students):
    student_totals = {}
    averages = {}
    passed_students = []
    top_student = ''
    subject_highest_marks = float('-inf')  # highest marks scored amongst all students in any subject
    highest_avg = float('-inf')

    for student in students:
        total_mark = 0
        mark_count = 0

        for mark in student['marks']:
            total_mark += mark
            mark_count += 1
            
            if mark > subject_highest_marks:
                subject_highest_marks = mark

        mark_average = total_mark/mark_count

        averages[student['name']] = mark_average
        student_totals[student['id']] = total_mark

        if mark_average >= 60:
            passed_students.append(student['name'])

        if mark_average > highest_avg:
            highest_avg = mark_average
            top_student = student['name']

    return {

        'student_totals': student_totals,
        'averages': averages,
        'passed_students': passed_students,
        'top_student': top_student,
        'subject_highest_marks': subject_highest_marks
        
    }    

print(get_student_details(students))