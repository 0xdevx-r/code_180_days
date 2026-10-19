# Find the largest number without using max()

numbers = [14, 7, 29, 3, 18, 11]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)