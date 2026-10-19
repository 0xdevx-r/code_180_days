''' Return:

"long_products" → products with more than 6 characters
"product_lengths" → list containing the character count of every product, in the same order
"e_products" → products containing the letter "e"
Manually count characters using a loop
Use loops
No len()
No list comprehensions
No count()
No filter()
Do not modify the original list
No print() inside the function'''

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam", "Headphones"]

def analyze_products(products):
    long_products = []
    product_lengths = []
    e_products = []

    for product in products:
        char_count = 0
        for char in product:
            char_count += 1
        product_lengths.append(char_count)

        if char_count > 6:
            long_products.append(product)

        if 'e' in product:
            e_products.append(product)

    return {

        "long_products": long_products,
        "product_lengths": product_lengths,
        "e_products": e_products
    }

print(analyze_products(products))