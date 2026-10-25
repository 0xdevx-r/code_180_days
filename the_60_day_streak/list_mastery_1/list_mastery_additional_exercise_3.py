'''
Return:
largest_order
Number of items in the largest order.

largest_order_customers
Every customer whose order has that largest number of items.
Preserve original order.

customers_with_mouse
Customers whose order contains "Mouse".
Preserve original order.

item_frequency
Frequency of every item across all orders.
Preserve first-appearance order.

unique_items
Unique items across all orders.
Preserve first-appearance order.

Restrictions
No:
len()
count()
sum()
set()
max()
sorted()
comprehensions
mutation of orders
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
        "items": ["Monitor", "Mouse", "Keyboard", "Webcam"]
    },
    {
        "id": "O103",
        "customer": "Rohan",
        "items": ["Laptop", "Mouse", "Keyboard"]
    },
    {
        "id": "O104",
        "customer": "Neha",
        "items": ["Mouse", "Mouse", "Webcam", "Keyboard", "Monitor"]
    },
    {
        "id": "O105",
        "customer": "Kabir",
        "items": ["Laptop"]
    },
    {
        "id": "O106",
        "customer": "Ishaan",
        "items": ["Mouse", "Keyboard", "Monitor", "Laptop", "Webcam"]
    }
]

def get_order_details(orders):

    largest_order = float('-inf')               # No. of items in largest order
    largest_order_customers = []                # customers with highest number of items
    customers_with_mouse = []                   # customers with mouse in order
    item_frequency = {}                         # item count across all orders
    unique_items = []                           # unique items across all orders

    for order in orders:
        item_count = 0

        for item in order['items']:
            item_count += 1

            if item not in unique_items:
                unique_items.append(item)

            if item not in item_frequency:
                item_frequency[item] = 1
            else:
                item_frequency[item] += 1

        if item_count > largest_order:
            largest_order = item_count
            largest_order_customers = [order['customer']]

        elif item_count == largest_order:
            largest_order_customers.append(order['customer'])

        if 'Mouse' in order['items']:
            customers_with_mouse.append(order['customer'])

    return {
        'largest_order': largest_order,
        'largest_order_customers': largest_order_customers,
        'customers_with_mouse': customers_with_mouse,
        'item_frequency': item_frequency,
        'unique_items': unique_items
    }
print(get_order_details(orders))