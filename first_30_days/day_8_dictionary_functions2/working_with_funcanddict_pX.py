
''' Requirements :-
    "low_stock" → products with stock <= threshold
    "total_items" → number of different products
    "highest_stock" → name of product with the highest stock
    Use one for loop
    Use .items()
    Do not use max()
    Do not use sum()
    Do not use sorted()
    Do not modify inventory
    Do not call previous functions
    No printing inside the function '''

inventory = {
    "laptop": 12,
    "mouse": 4,
    "keyboard": 8,
    "monitor": 2,
    "headphones": 15,
    "webcam": 3
}

def get_stock_data(inventory, threshold):
    low_stock = []
    total_items = 0
    highest_stock = ""
    highest_stock_count = 0
    stock_dictionary = {}

    for name, count in inventory.items():
        if count <= threshold:
            low_stock.append(name)
        total_items = len(inventory.items())
        if count > highest_stock_count:
            highest_stock_count = count
            highest_stock = name
    stock_dictionary.update({"low_stock": low_stock})
    stock_dictionary.update({"total_items": total_items})
    stock_dictionary.update({"highest_stock": highest_stock})
    return stock_dictionary

print(get_stock_data(inventory,4))