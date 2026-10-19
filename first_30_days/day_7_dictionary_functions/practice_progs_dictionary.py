# this is a combined program where:
# we will read a dictionary
# Change the value
# update through a function
# check data - true/false
# add data through a function
# dictionary+loop > we will count values
# finding highest score in the dictionary


# reading a dictionary

employees = {"emp1":"Ron", "access_level":"Intern", "emp2":"Bert", "access_level2":"Manager"}
print(employees["access_level"])

# changing the value of access_level to Team Lead
employees["access_level"] = "Team Lead"
print(employees["access_level"])

# alternatively
employees.update({'access_level':'Team Lead'})
print(employees["access_level"])

# updating through a function

def update_emp_access(employees):
    employees.update({"access_level2" : "Senior Manager"})
    return employees
print(update_emp_access(employees)["access_level2"])

# check data - true/false

def check_access_level(employees):
    return employees["access_level"] != "Developer"

print(check_access_level(employees))

# add data through a function

def add_emp_data(employees):
    employees.update({"employment1": "Contractual", "employment2": "Permananet"})
    return employees

print(add_emp_data(employees))

# dictionary+loop > we will count values

scores = {
    "Alex": 85,
    "John": 42,
    "Mike": 76,
    "Sara": 91,
    "Tom": 38
}
def count_passed_student(scores):
    count = 0
    for values in scores.values():
        if values >= 50:
            count += 1
    return count
print(count_passed_student(scores))