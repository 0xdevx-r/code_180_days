'''
Return
unique_products → set of unique product names
category_products → Category → list of product names, preserving first-seen order without duplicates
category_counts → Category → number of products in that category, counting each unique product once
expensive_products → set of product names priced at ₹10,000 or above
price_by_product → Product → price

Restrictions: No len(), count(), sum(), max(), min(), sorted(), or comprehensions. No mutation of products; no print() inside the function.'''


products = [
    ("Laptop", "Electronics", 75000),
    ("Mouse", "Electronics", 1200),
    ("Chair", "Furniture", 8500),
    ("Keyboard", "Electronics", 2500),
    ("Desk", "Furniture", 12000),
    ("Monitor", "Electronics", 18000),
    ("Mouse", "Electronics", 1200),
    ("Chair", "Furniture", 8500)
]

def get_product_details(products):
    unique_products = set()
    category_products = {}
    category_counts = {}
    expensive_products = set()
    price_by_product = {}
    
    for product, category, price in products:
        if product not in unique_products:
            unique_products.add(product)

            if category not in category_products:
                category_products[category] = []
            category_products[category].append(product)

            if category not in category_counts:
                category_counts[category] = 1
            else:
                category_counts[category] += 1

        if price >= 10000:
            expensive_products.add(product)

        price_by_product[product] = price
        

    return {'unique_products': unique_products,
            'category_products': category_products,
            'category_counts': category_counts,
            'expensive_products': expensive_products,
            'price_by_product': price_by_product
            }
print(get_product_details(products))