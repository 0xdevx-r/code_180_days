# function to calculate square of a number

def calculate_square(number):
    return number * number

user_input = int(input("Enter a whole number: "))

result = calculate_square(user_input)
print(f"The square is : {result}")
