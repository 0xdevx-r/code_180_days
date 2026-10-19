# Vowel counting

#defining vowels
vowel = "aeiouAEIOU"

#initializing count from 0 
count = 0

user_input = input("Enter your sentence: ")
for char in user_input:
    if char in vowel:
        count += 1
print(f"{count} is total number for vowels.")
