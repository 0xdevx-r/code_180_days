'''
Return a dictionary containing:
customers_with_multiple_items. 
Customers whose order contains more than 2 items
Preserve original order

item_counts_per_order
Dictionary mapping order ID → number of items
Count manually

unique_items
Every distinct item across all orders
Preserve first-appearance order

total_item_count
Total number of items across every order
Count manually

Restrictions
Do not use:
len()
count()
sum()
set()
max()
sorted()
list/dict comprehensions
mutation of the input orders
print() inside the function'''

orders = [
    {
        "id": "O101",
        "customer": "Aarav",
        "items": ["Mouse", "Keyboard"]
    },
    {
        "id": "O102",
        "customer": "Maya",
        "items": ["Monitor", "Mouse", "Keyboard"]
    },
    {
        "id": "O103",
        "customer": "Rohan",
        "items": ["Laptop"]
    },
    {
        "id": "O104",
        "customer": "Neha",
        "items": ["Mouse", "Mouse", "Webcam", "Keyboard"]
    },
    {
        "id": "O105",
        "customer": "Kabir",
        "items": ["Monitor", "Webcam"]
    }
]

def get_order_details(orders):
    customers_with_multiple_items = []
    item_counts_per_order = {}
    unique_items = []
    total_item_count = 0

    for order in orders:
        item_count = 0

        for item in order['items']:
            item_count += 1
            total_item_count += 1
            item_counts_per_order[order['id']] = item_count

            if item not in unique_items:
                unique_items.append(item)

        if item_count > 2:
            customers_with_multiple_items.append(order['customer'])

            
    return {
        'item_counts_per_order': item_counts_per_order,
        'customers_with_multiple_items': customers_with_multiple_items,
        'unique_items': unique_items,
        'total_item_count': total_item_count}

print(get_order_details(orders))
        