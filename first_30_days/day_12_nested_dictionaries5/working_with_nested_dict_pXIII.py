'''Return the total quantity of all products
    Use .values()
    Use a for loop
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

def get_total_stock(inventory):
    total = 0
    for value in inventory.values():
        total += value
    return total
print(get_total_stock(inventory))
