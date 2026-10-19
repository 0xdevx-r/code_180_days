""" Requirements:

    Return a list of item names whose stock is less than or equal to threshold.
    Use .items().
    Use a for loop.
    Do not modify inventory.
    Do not use sorted(), min(), or max().
    The threshold must come from the function parameter.
    Do not print inside the function. """

# creating dictionary of items

inventory = {
    "laptop": 12,
    "mouse": 4,
    "keyboard": 8,
    "monitor": 2,
    "headphones": 15
}

#creating function with parameters

def get_item_list(inventory, threshold):
    stock_list = []
    for item, quantity in inventory.items():
        if quantity <= threshold:
            stock_list.append(item)
    return stock_list

print(get_item_list(inventory,2))