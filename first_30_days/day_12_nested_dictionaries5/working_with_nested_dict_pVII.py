'''Requirements:
   - find the product with the highest stock.
    Return the product name with the highest stock
    Use .items()
    Use a for loop
    Do not use max()
    Do not use sorted()
    Do not modify inventory
    Do not print inside the function'''

inventory = {
    "laptop": 12,
    "mouse": 4,
    "keyboard": 8,
    "monitor": 2,
    "headphones": 15,
    "webcam": 3
}

def get_highest_stock_product(inventory):
    highest_stock = float("-inf")
    highest_stock_product = ''
    for key,value in inventory.items():
        if value > highest_stock:
            highest_stock = value
            highest_stock_product = key
    return highest_stock_product

print(get_highest_stock_product(inventory))
