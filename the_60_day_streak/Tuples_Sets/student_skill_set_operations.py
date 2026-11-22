'''Return
all_skills → set of all unique skills
python_sql_users → set of students who know both Python and SQL
python_or_docker_users → set of students who know Python or Docker
exclusive_python_users → set of students who know Python but not Docker
skill_users → Skill → set of students who know that skill
Restrictions: No len(), count(), sum(), max(), min(), sorted(), or comprehensions. 
No mutation of students; no print() inside the function.'''

students = [
    ("Aarav", ("Python", "SQL", "Git")),
    ("Maya", ("HTML", "CSS", "JavaScript")),
    ("Rohan", ("Python", "Docker", "Git")),
    ("Neha", ("Python", "SQL", "Pandas")),
    ("Kabir", ("SQL", "Git", "Docker")),
    ("Ishaan", ("Python", "Pandas", "Docker"))
]

def get_student_details(students):
    all_skills = set()
    python_sql_users = set()
    python_or_docker_users = set()
    exclusive_python_users = set()
    skill_users = {}

    for name, skills in students:
        all_skills.update(skills)     
        
        if 'Python' in skills and 'SQL' in skills:
            python_sql_users.add(name)

        if 'Python' in skills or 'Docker' in skills:
            python_or_docker_users.add(name)

        if 'Python' in skills and 'Docker' not in skills:
            exclusive_python_users.add(name)

        for skill in skills:
            if skill not in skill_users:
                skill_users[skill] = set()
            skill_users[skill].add(name)

    return {'all_skills': all_skills,
            'python_sql_users': python_sql_users,
            'python_or_docker_users': python_or_docker_users,
            'exclusive_python_users': exclusive_python_users,
            'skill_users': skill_users
    }
print(get_student_details(students))