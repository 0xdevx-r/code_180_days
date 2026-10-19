# Sum of Numbers in a Range


while True:
    try:
        user_input = int(input("Enter the range: "))
        print(f"Entered range : {user_input}")
        break
    except ValueError:
        print("Enter a valid number. Try again.")


number_sum = 0

for num in range(user_input):
    number_sum += num

print(f"Sum of numbers in range {user_input} is: {number_sum}  ")