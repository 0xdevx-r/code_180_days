# Takes an integer from the user.
# If the number is between 1 and 100 inclusive, continue.
# Otherwise print "Invalid range."
# For a valid number - print "Even" for even and "Odd" for Odd
# if the number is divisible by both 3 and 5, print "FizzBuzz" instead.

user_input = int(input("Enter the number: "))

def odd_even(num):
    return num % 2 == 0

if 1 <= user_input <= 100:
    if user_input % 3 == 0 and user_input % 5 == 0:
        print("FizzBuzz")
    else: 
        if odd_even(user_input):
            print("Even.")
        else:
            print("Odd.")
else:
    print("Invalid Range.")
