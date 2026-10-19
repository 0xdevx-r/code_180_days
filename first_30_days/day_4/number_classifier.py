# generating a number classifier
# finding given number from user is negative, positive or zero

while True:
    try:
        user_input = int(input("Enter the number: "))
        break
    except ValueError:
        print("Valid number required.")

if  user_input > 0:
    print("Positive.")

elif user_input < 0:
    print("Negative.")

else:
    print("Zero.")