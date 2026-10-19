'''Requirements:

    Return a list of item names whose stock is ≤ threshold
    Use .items()
    Use a for loop
    Do not modify inventory
    Do not use sorted()
    Do not use previous functions
    Do not print inside the function'''

# Creating the dictionary

inventory = {
    "laptop": 12,
    "mouse": 4,
    "keyboard": 8,
    "monitor": 2,
    "headphones": 15,
    "webcam": 3
}

def get_low_stock_items(inventory,threshold):

    item_list = []
    for key, value in inventory.items():
        if value <= threshold:
            item_list.append(key)
    return item_list

print(get_low_stock_items(inventory,4))
