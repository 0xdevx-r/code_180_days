'''Requirements:

    Return the number of products whose stock is <= threshold
    Use .values()
    Use a for loop
    Do not use len()
    Do not use sum()
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

def get_low_stock_count(inventory,threshold):
    item_count = 0
    for value in inventory.values():
        if value <= threshold:
            item_count += 1
    return item_count

print(get_low_stock_count(inventory, 4))