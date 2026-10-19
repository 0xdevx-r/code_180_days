''' RETURN:
"digit_counts" → dictionary mapping each product ID → number of digits in its product name
"electronics" → list of product names whose category is "Electronics"
"name_lengths" → dictionary mapping each product ID → length of its product name

Requirements: 

Use .items()
Use loops
Manually count digits
Use .isnumeric() or another appropriate character check
No count()
No list comprehensions
No previous functions
Do not modify products
No print() inside the function
Return exactly the 3 required keys'''

products = {
    "P101": {"name": "Laptop Pro 15", "category": "Electronics"},
    "P102": {"name": "Office Desk 2", "category": "Furniture"},
    "P103": {"name": "Wireless Mouse 3", "category": "Electronics"},
    "P104": {"name": "Desk Lamp", "category": "Furniture"},
    "P105": {"name": "Gaming Keyboard 7", "category": "Electronics"}
}

def get_product_details(products):
    digit_counts = {}
    electronics = []
    name_lengths = {}

    for key, value in products.items():
        if value['category'] == 'Electronics':
            electronics.append(value['name'])

        char_count = 0
        for char in value['name']:
            char_count += 1
        name_lengths[key] = char_count

        digit_count = 0
        for digit in value['name']:
            if digit.isnumeric():
                digit_count += 1
            digit_counts[key] = digit_count
    return {

        "digit_counts": digit_counts,
        "electronics": electronics,
        "name_lengths": name_lengths
    }

print(get_product_details(products))