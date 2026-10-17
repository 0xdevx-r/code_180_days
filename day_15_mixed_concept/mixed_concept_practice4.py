''' RETURN

"mouse_orders" → customer names whose order contains "Mouse".
"item_counts" → dictionary mapping each order ID to its total number of items, including duplicates.
"customer_names" → list of all customer names, in order."

REQUIREMENTS:
Use .items() and .split().
Use loops and manually count items.
No count(), no list comprehensions, no previous functions.
Do not modify orders.
No print() inside the function.
Return exactly the three required keys.
'''
orders = {
    "O101": {"customer": "Aarav", "items": "Mouse, Keyboard, Mouse"},
    "O102": {"customer": "Maya", "items": "Monitor, Mouse"},
    "O103": {"customer": "Rohan", "items": "Keyboard, Keyboard"},
    "O104": {"customer": "Neha", "items": "Laptop, Mouse, Monitor"},
    "O105": {"customer": "Kabir", "items": "Laptop, Keyboard"}
}

def get_customer_details(orders):
    mouse_orders = []
    item_counts = {}
    customer_names = []

    for order_id, order_details in orders.items():
        customer_names.append(order_details['customer']) 

        item_count = 0
        
        if 'Mouse' in order_details['items'].split(', '):
            mouse_orders.append(order_details['customer'])

        for item in order_details['items'].split(', '):
            item_count  += 1
        item_counts[order_id] = item_count

        
    
    return {
        
        "mouse_orders": mouse_orders,
        "item_counts": item_counts,
        "customer_names": customer_names
    }

print(get_customer_details(orders))