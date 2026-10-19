#Write a program that accepts a number from 1–100 and prints:

# "FizzBuzz" → divisible by 3 AND 5
# "Fizz" → divisible by 3 only
# "Buzz" → divisible by 5 only
# "Even" → even but not divisible by 3 or 5
# "Odd" → odd and not divisible by 3 or 5
# "Invalid Range" → outside 1–100
while True:
    
    try:
        user_input = int(input("Enter the number between 1-100: "))

        if 1 <= user_input <= 100:
            print(f"Entered number : {user_input}")
            break
        else:
            print("Invalid Range")
    except ValueError:
        print("Invalid entry. Try entering a number.")

if user_input % 3 == 0 and user_input % 5 == 0:
    print("FizzBuzz")

elif user_input % 3 == 0:
    print("Fizz")

elif user_input % 5 == 0:
    print("Buzz")

elif user_input % 2 == 0:
    print("Even")

else:
    print("Odd")