# Number Classifier Function

def classify_number(num): 
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"
    
user_input = int(input("Enter the number to check: "))
print(classify_number(user_input))