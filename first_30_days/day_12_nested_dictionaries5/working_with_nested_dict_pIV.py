'''Return product names with price greater than price_limit
    Use .items()
    Use a for loop
    Do not use sorted()
    Do not modify inventory
    Do not print inside the function'''

inventory = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "monitor": 300,
    "headphones": 150,
    "webcam": 90
}

def get_expensive_products(inventory,price_limit):
    product_names = []
    for key,value in inventory.items():
        if value > price_limit:
            product_names.append(key)
    return product_names

print(get_expensive_products(inventory, 100))