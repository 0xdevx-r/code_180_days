''' RETURN:

"mouse_customers" → customer names whose order contains "Mouse".
"item_counts" → dictionary mapping each order ID to the number of items, including duplicates.
"customer_name_lengths" → dictionary mapping each order ID to the number of characters in the customer's name.

Requirements
Use .items(), .split() and loops.
Manually count items and name characters.
No count(), no list comprehensions, no previous functions.
Do not modify orders.
No print() inside the function.
Return exactly the three required keys.'''

orders = {
    "O101": {"customer": "Aarav", "items": "Mouse, Keyboard, Mouse"},
    "O102": {"customer": "Maya", "items": "Monitor, Mouse"},
    "O103": {"customer": "Rohan", "items": "Keyboard, Keyboard"},
    "O104": {"customer": "Neha", "items": "Laptop, Mouse, Monitor"},
    "O105": {"customer": "Kabir", "items": "Laptop, Keyboard"}
}

def get_customer_details(orders):
    mouse_customers = []
    item_counts = {}
    customer_name_lengths = {}

    for key,value in orders.items():
        if 'Mouse' in value['items'].split(', '):
            mouse_customers.append(value['customer'])

        item_count = 0
        for item in value['items'].split(', '):
            item_count += 1
        item_counts[key] = item_count

        name_char_count = 0
        for char in value['customer']:
            name_char_count += 1
        customer_name_lengths[key] = name_char_count

    return{
        "mouse_customers": mouse_customers,
        "item_counts": item_counts,
        "customer_name_lengths": customer_name_lengths
    }

print(get_customer_details(orders))