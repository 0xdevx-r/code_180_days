''' "positive_numbers" → all numbers greater than 0
"negative_numbers" → all numbers less than 0
"doubled_numbers" → every number multiplied by 2, preserving the original order
"zero_count" → the number of zeros, counted manually with a loop

Restrictions: Use loops, no list comprehensions
no count(), no filter(), no len(), 
and do not modify the original list. 
No print() inside the function.'''

numbers = [12, -5, 0, 8, -3, 17, 4, -10, 6, 0]

def analyze_nums(numbers):
    positive_numbers = []
    negative_numbers = []
    doubled_numbers = []
    zero_count = 0

    for num in numbers:
        if num > 0:
            positive_numbers.append(num)

        elif num < 0:
            negative_numbers.append(num)

        if num == 0:
            zero_count += 1

        doubled_numbers.append(num*2)

    return {

        'positive_numbers': positive_numbers,
        'negative_numbers': negative_numbers,
        'doubled_numbers': doubled_numbers,
        'zero_count': zero_count
    }

print(analyze_nums(numbers))