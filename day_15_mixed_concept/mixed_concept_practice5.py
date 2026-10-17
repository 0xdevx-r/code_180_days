''' RETURN:

portable_products" → product names whose tags contain "portable".
"tag_counts" → dictionary mapping each product ID to its number of tags.
"name_digit_counts" → dictionary mapping each product ID to the number of digits in its product name.

TREQUIREMENTS:
Use .items(), .split(), and loops.
Manually count tags and digits.
No count(), no list comprehensions, no previous functions.
Do not modify products.
No print() inside the function.
Return exactly the three required keys.'''

products = {
    "P101": {"name": "Laptop Pro", "tags": "electronics, premium, portable"},
    "P102": {"name": "Wireless Mouse", "tags": "electronics, wireless"},
    "P103": {"name": "Office Desk", "tags": "furniture, wooden"},
    "P104": {"name": "Gaming Keyboard", "tags": "electronics, gaming, wired"},
    "P105": {"name": "Desk Lamp", "tags": "furniture, portable"}
}

def get_product_details(products):
    portable_products = []
    tags_counts = {}
    name_digit_counts = {}

    for key,value in products.items():
        tag_count = 0

        if 'portable' in value['tags'].split(', '):
            portable_products.append(value['name'])

        
        for tag in value['tags'].split(', '):
            tag_count += 1

        tags_counts[key] = tag_count

        prod_name_digit = 0

        for char in value['name']:
            if char.isnumeric():
                prod_name_digit += 1
                
        name_digit_counts[key] = prod_name_digit

    return {
        "portable_products": portable_products,
        "tag_counts": tags_counts,
        "name_digit_counts": name_digit_counts
    } 

print(get_product_details(products))