# Even/Odd Function
# Write a function

def check_odd_even(num):
    return num % 2 == 0

user_input = int(input("Enter the number: "))

result = check_odd_even(user_input)
if result:
    print("Even")
else:
    print("Odd")