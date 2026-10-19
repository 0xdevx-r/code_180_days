''' Constraints
    Use .items()
    Use one for loop
    Do not use max()
    Do not use sorted()
    Do not use dictionary comprehension
    Do not modify inventory
    Do not call previous functions
    Do not use print()
    Follow the exact output contract'''

# For threshold = 5, return a dictionary containing:
# "low_stock" → item names where stock is ≤ threshold
# "total_items" → number of different products
# "highest_stock" → name of the product with the highest stock

inventory = {
    "phone": 7,
    "tablet": 3,
    "charger": 12,
    "keyboard": 5,
    "camera": 9,
    "cable": 2,
    "speaker": 6
}

def get_item_details(inventory, threshold):
    low_stock = []
    total_items = 0
    highest_stock = ""
    highest_stock_count = 0

    for name, item_count in inventory.items():
        if item_count <= threshold:
            low_stock.append(name)
        total_items = len(inventory)
        if item_count > highest_stock_count:
            highest_stock_count = item_count
            highest_stock = name
            
    inventory_dictionary = {
        "low stock": low_stock,
        "total_items": total_items,
        "highest_stock": highest_stock
    }
    return inventory_dictionary

print(get_item_details(inventory, 5))