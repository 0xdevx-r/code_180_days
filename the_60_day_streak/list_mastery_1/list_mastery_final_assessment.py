'''

Requirements

customers_with_mouse
Customers whose order contains "Mouse".
Preserve original order.

item_frequency
Dictionary containing the frequency of every item across all orders.
Count duplicates.
Example: if "Mouse" appears 5 times total → "Mouse": 5.

unique_items
Every distinct item exactly once.
Preserve the order in which each item first appears across the orders.

largest_order
the largest number of items in any order.
Count manually.
No len().

largest_order_customer- list of every customer whose order has that many items, preserving original order.

Restrictions
Use loops.
Use conditions.
Manually count where required.
No len()
No count()
No sum()
No max()
No sorted()
No set()
No list comprehensions.
Do not modify orders.
No print() inside the function.
Return exactly the five required keys.'''

orders = [
    {"id": "O101", "customer": "Aarav", "items": ["Mouse", "Keyboard", "Mouse"]},
    {"id": "O102", "customer": "Maya", "items": ["Monitor", "Mouse"]},
    {"id": "O103", "customer": "Rohan", "items": ["Keyboard", "Keyboard", "Mouse"]},
    {"id": "O104", "customer": "Neha", "items": ["Laptop", "Mouse", "Monitor"]},
    {"id": "O105", "customer": "Kabir", "items": ["Laptop", "Keyboard"]}
]

def get_order_details(orders):
    customers_with_mouse = []
    item_frequency = {}
    unique_items = []
    largest_order = float('-inf')
   
    largest_order_customers = []

    for order_details in orders:
        customer_order_size = 0
        if 'Mouse' in order_details['items']:
            customers_with_mouse.append(order_details['customer'])

        for item in order_details['items']:
            customer_order_size += 1

            if item not in item_frequency:
                item_frequency[item] = 1
            else:
                item_frequency[item] += 1

            if item not in unique_items:
                unique_items.append(item)

        if customer_order_size > largest_order:
            largest_order = customer_order_size
            largest_order_customers.append(order_details['customer'])
            
        elif customer_order_size == largest_order:
            largest_order_customers.append(order_details["customer"])
    
    return {

    'customers_with_mouse': customers_with_mouse,
    'item_frequency': item_frequency,
    'unique_items': unique_items,
    'largest_order': largest_order,
    'largest_order_customers': largest_order_customers
}        
print(get_order_details(orders))