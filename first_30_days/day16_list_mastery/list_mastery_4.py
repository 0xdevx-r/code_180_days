'''
"common_items" → items present in both lists, each listed once, 
preserving their first appearance order in list_a

"only_a" → items present in list_a but not in list_b, each listed once, 
preserving first appearance order

"only_b" → items present in list_b but not in list_a, each listed once, 
preserving first appearance order

"unique_a_count" → number of distinct items in list_a, counted manually
"unique_b_count" → number of distinct items in list_b, counted manually

Restrictions
Use loops and conditions.
No set(), len(), count(), sorted(), or list comprehensions.
Do not modify either input list.
No print() inside the function.
Return exactly these five keys.'''

list_a = [12, 5, 8, 5, 20, 3, 12, 7]
list_b = [5, 9, 12, 15, 3, 3, 18]

def analyze_lists(list_a, list_b):
    common_items = []
    only_a = []
    only_b = []
    unique_a_count = 0
    unique_a = []
    unique_b_count = 0
    unique_b = []

    for num_a in list_a:
        if num_a in list_b and num_a not in common_items:
            common_items.append(num_a)

        if num_a not in list_b and num_a not in only_a:
            only_a.append(num_a)

        if num_a not in unique_a:
            unique_a.append(num_a)
            unique_a_count += 1

    for num_b in list_b:
        if num_b not in list_a and num_b not in only_b:
            only_b.append(num_b)

        if num_b not in unique_b:
            unique_b.append(num_b)
            unique_b_count += 1    

    return {
        'common_items': common_items,
        'only_a': only_a,
        'only_b': only_b,
        'unique_a_count': unique_a_count,
        'unique_b_count': unique_b_count
    }

print(analyze_lists(list_a, list_b))