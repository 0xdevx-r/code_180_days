# Count Vowels Function

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
user_input = input("Enter the sentence: ")
print(f"Count of Vowels: {count_vowels(user_input)}") 