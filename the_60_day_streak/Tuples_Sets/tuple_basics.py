'''Return
- student_names → tuple of all student names, original order
- subjects → tuple of all subjects, original order
- subject_students → set of unique subjects
- high_scorers → tuple of student names scoring 85 or above
- score_by_student → dictionary mapping student name → score
Restrictions: No len(), count(), sum(), max(), min(), sorted(), or comprehensions. No mutation of students; no print() inside the function'''

students = [
    ("Aarav", "Python", 85),
    ("Maya", "Python", 92),
    ("Rohan", "SQL", 78),
    ("Neha", "Python", 88),
    ("Kabir", "SQL", 91),
    ("Ishaan", "Git", 80)
]

def get_students_detail(students):
    student_names = ()
    subjects = ()
    subject_students = set()
    high_scorers = ()
    score_by_student = {}

    for name, subject, score in students:
        student_names += (name,)
        subjects += (subject,)
        
        subject_students.add(subject)
        score_by_student[name] = score
        
        if score >= 85:
            high_scorers += (name,)

    return {
        'student_names': student_names,
        'subjects': subjects,
        'high_scorers': high_scorers,
        'subject_students': subject_students,
        'score_by_student': score_by_student
    }

print(get_students_detail(students))