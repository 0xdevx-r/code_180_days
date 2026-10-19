# Reverse String without slicing

user_input = input("Enter the sentence to reverse: ")

reversed_string = " "

for char in user_input:
    reversed_string = char + reversed_string
print(f"Reversed string is: {reversed_string}")