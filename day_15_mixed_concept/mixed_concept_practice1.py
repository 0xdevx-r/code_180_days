
'''Write a function analyze_products(products) that returns a dictionary containing exactly:
"digit_count" → total number of "digit" characters in all product names.
"name_lengths" → dictionary mapping each product ID to the length of its product name, excluding leading/trailing spaces if any.
"electronics" → list of product names whose category is "Electronics".'''


products = {
        
    "P102": {"name": "Mouse 2", "category": "Electronics"},
    "P103": {"name": "Desk 1", "category": "Furniture"},
    "P104": {"name": "Chair 4", "category": "Furniture"},
    "P105": {"name": "Monitor 5", "category": "Electronics"}
}

def analyze_products(products):

    digit_count = 0                  # counts number of digit character in dictionary value
    name_lengths = {}                 # counts characters in each product name
    electronics = []                 # list of all the products which are in Electronics category
    
    
    for key,value in products.items():
        for char in value['name']:
            if char.isdigit():
                digit_count += 1

        name_len_count = 0
        for char in value['name']:
            name_len_count += 1
            name_lengths.update({key: name_len_count})
             

        if value['category'] == 'Electronics':
                electronics.append(value['name'])

    return {

        "digit_count" : digit_count,
        "name_lengths" : name_lengths,
        "electronics" : electronics
    }

print(analyze_products(products))
