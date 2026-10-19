# count Vowels
# a 45 min coding practice to check the repition and understanding of the code

# taking user input as string

while True:
    user_input = input("Enter the stentence: ").strip()
    if user_input:
        break
    print("Enter a valid sentence.")

# declaring Vowels and a Vowel counter

vowels = "aeiouAEIOU"
vowel_counter = 0

for char in user_input:
    if char in vowels:
        vowel_counter += 1

print(f"Vowel count is: {vowel_counter}")