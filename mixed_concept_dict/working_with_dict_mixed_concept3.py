''' RETURN:

"portable_products" → product names whose tags contain "portable".
"tag_counts" → dictionary mapping each product ID to its number of tags.
"name_digit_counts" → dictionary mapping each product ID to the number of digits in its product name.

Requirements
Use .items(), .split() and loops.
Manually count tags and digits.
No count(), no list comprehensions, no previous functions.
Do not modify products.
No print() inside the function.
Return exactly the three required keys.'''

products = {
    "P101": {"name": "Laptop Pro 15", "tags": "electronics, premium, portable"},
    "P102": {"name": "Wireless Mouse 3", "tags": "electronics, wireless"},
    "P103": {"name": "Office Desk 2", "tags": "furniture, wooden"},
    "P104": {"name": "Gaming Keyboard 7", "tags": "electronics, gaming, wired"},
    "P105": {"name": "Desk Lamp", "tags": "furniture, portable"}
}

def product_data(products):
    portable_products = []
    tag_counts = {}
    name_digit_counts = {}

    for key,value in products.items():
        if 'portable' in value['tags']:
            portable_products.append(value['name'])

        tags = 0
        for item in value['tags'].split(', '):
            tags += 1
        tag_counts[key] = tags

        char_digit = 0
        for char in value['name']:
            if char.isnumeric():
                char_digit += 1
        name_digit_counts[key] = char_digit

    return {

        "portable_products": portable_products,
        "tag_counts": tag_counts,
        "name_digit_counts": name_digit_counts
    }

print(product_data(products))
