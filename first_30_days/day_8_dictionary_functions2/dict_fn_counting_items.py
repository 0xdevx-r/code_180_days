
# Return the number of different products.
# Do not calculate total stock.
# Do not use sum().
# Do not use a loop for this one.
# Do not modify inventory.

inventory = {"laptop": 12, "mouse": 4, "keyboard" : 8, "monitor": 2}

def get_product_count(inventory):
    product_count = len(inventory)
    return product_count

print(get_product_count(inventory))