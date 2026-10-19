'''Requirements:

    Return a new dictionary containing only products whose price is greater than price_limit.
    Preserve the original product names and prices.
    Use .items().
    Use a for loop.
    Do not modify the original dictionary.
    Do not use dictionary comprehension.
    Do not use filter(), sorted(), max(), etc.'''

# creating initial dictionary with products and prices

products = {
    "laptop": 65000,
    "mouse": 1200,
    "keyboard": 2500,
    "monitor": 18000,
    "headphones": 5000
}

# defining a new dictionary with product and price_limit as param.

def get_product_details(products, price_limit):
    new_product_dictionary = {}
    for name, price in products.items():
        if price > price_limit:
            new_product_dictionary.update({name : price})
    return new_product_dictionary

print(get_product_details(products, 5000))