#checking if a number is odd or even

user_input = int(input("Enter the number to check: "))
if user_input% 2 == 0:
    print(f"{user_input} is even!")
else:
    print(f"{user_input} is odd.")