# adding different sample practice examples of defining a function

def square(num):
    return num*num

def is_positive(number):
    return number > 0
    

def count_items(items):
    item_count = 0
    for item in items:
        item_count += 1
    return item_count


def find_largest(numbers):
    largest_num = numbers[0]
    for num in numbers:
        if num > largest_num:
            largest_num = num
    return largest_num


def calculate_sum(numbers):
    num_sum = 0
    for num in numbers:
        num_sum += num
    return num_sum    

def count_even(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    return even_count

def get_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_list = []
    for char in text:
        if char in vowels:
            vowel_list.append(char)
    return vowel_list

def double_numbers(numbers):
    # return a new list where every number is doubled
    doubled_list = []
    for num in numbers:
        doubled_list.append(num*2)
    return doubled_list

def get_positive(numbers):
    # return a new list containing only positive numbers
    postive_num_list = []
    for num in numbers:
        if num > 0:
            postive_num_list.append(num)
    return postive_num_list

def find_shortest_word(words):
    # return the shortest word
    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word
    
        