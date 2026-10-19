# Largest number without max()
# using while loop to take valid input from user
# Valid input is an interger for this case.
# using try and except ValueError to counter the errors for string or no input

while True:
    try:
        number_range = int(input("Total number count: "))
        if number_range > 0:
            print(f"Range of number - {number_range}")
            break
        else:
            print("Enter a valid range.")
    except ValueError:
        print("Enter a valid integer.")

# list to store the user input numbers in given range

number_list = []

# using for loop to : loop till the range - 1 and append it in the number_list
# printing the list later for user
# using number_list.clear() to remove the old entries in case of ValueError handling 

while True:
    try:
        for num in range(number_range):
            entered_num = int(input(f"Enter number {num+1}: "))
            number_list.append(entered_num)
        print(f"Entered number list {number_list}")
        break
    except ValueError:
        print("Valid input number is required. Try again")
        number_list.clear()

# assigning a variable which will hold the highest number in created list
# assigning 0 as the highest number

largest_num = number_list[0]

for num in number_list:
    if num > largest_num:
        largest_num = num      
print(f"Largest number {largest_num}")

# adding a repttiotion block feature which allows users to select post completing first check
# the whole code block will repeat
# using boolean True and False with while to check user answer
# converting Y and N to lower to handle error in case user enters the lower case Y or N

repition_check = input("Do you want to try again? Y/N: ")

while True:
        
    if repition_check.lower() == "y":

        while True:
            try:
                number_range = int(input("Total number count: "))
                if number_range > 0:
                    print(f"Range of number - {number_range}")
                    break
                else:
                    print("Enter a valid range.")
            except ValueError:
                print("Enter a valid integer.")

        number_list = []

        while True:
            try:
                for num in range(number_range):
                    entered_num = int(input(f"Enter number {num+1}: "))
                    number_list.append(entered_num)
                print(f"Entered number list {number_list}")
                break
            except ValueError:
                print("Valid input number is required. Try again")
                number_list.clear()

        largest_num = number_list[0]

        for num in number_list:
            if num > largest_num:
                largest_num = num      
        print(f"Largest number {largest_num}")
        break

    elif repition_check.lower() == "n":
        print("Exiting..")
        break
               
    else:
        print("Choose Y or N!")
