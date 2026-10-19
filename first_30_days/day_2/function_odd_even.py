#  function to check even num

def is_even(num):
    return num % 2 == 0

user_num = int(input("Enter a whole number: "))

result = is_even(user_num)
if result:
    print("The number is Even.")
else:
    print("The number is Odd.")