'''Requirements:
Return a dictionary with exactly these keys:
total_stock → total quantity of all products
low_stock_count → number of products with stock <= threshold
low_stock_items → names of products with stock <= threshold
Use .items()
Use one for loop
Do not use sum(), len(), or sorted()
Do not modify inventory
Do not call your previous functions
Do not print inside the function
Exact output keys matter.'''

inventory = {
    "laptop": 12,
    "mouse": 4,
    "keyboard": 8,
    "monitor": 2,
    "headphones": 15,
    "webcam": 3
}

def get_inventory_details(inventory,threshold):
    total_stock = 0
    low_stock_count = 0
    low_stock_items = []
    for key,value in inventory.items():
        if value <= threshold:
            low_stock_count += 1
            low_stock_items.append(key)
        total_stock += value
    return {
        "total_stock": total_stock,
        "low_stock_count": low_stock_count,
        "low_stock_items": low_stock_items
    }
print(get_inventory_details(inventory,4))