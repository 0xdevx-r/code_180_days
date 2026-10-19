# function composition 
# function for square of the number and checking odd/evem

def calculate_square(num):
    return num**2
def is_even(num):
    return num % 2 == 0

user_input = int(input("Enter a whole number: "))
square = calculate_square(user_input)
even_odd = is_even(user_input)

print(f"Square: {square}")
print(f"Is the number even? {even_odd}")