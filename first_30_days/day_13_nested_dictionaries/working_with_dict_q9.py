'''Write a function that returns the names of products whose total sales are greater than their current stock.

Requirements:

Use .items().

Use a loop to calculate each product's total sales.

Do not use sum(), len(), max(), or sorted().

Do not use list comprehensions.

Do not modify inventory.

Do not print inside the function.'''

inventory = {
    "laptop": {"stock": 5, "sales": [2, 1, 3]},
    "mouse": {"stock": 12, "sales": [4, 2]},
    "keyboard": {"stock": 3, "sales": [1, 1, 1, 2]},
    "monitor": {"stock": 8, "sales": [2, 3]},
    "webcam": {"stock": 4, "sales": [1, 2, 1]}
}

def get_product_data(inventory):

    product_list = []
    for key,value in inventory.items():
        total_sales = 0
        for sale in value['sales']:
            total_sales += sale
        if total_sales > value['stock']:
            product_list.append(key)
    return product_list

print(get_product_data(inventory))