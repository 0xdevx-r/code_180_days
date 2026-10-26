'''
Return:

delivered_customers
Customers whose order status is "Delivered".
Preserve original order.

order_item_counts
Order ID → number of items.
Count manually.

pending_orders
Order IDs whose status is "Pending".
Preserve original order.

customer_item_totals
Customer → total number of items ordered.

customers_with_mouse
Customers whose order contains "Mouse".
Preserve original order.
Restrictions
No:
len(), count(), sum(), max(), min(), sorted(), set(), comprehensions, mutation of orders
print() inside the function'''

orders = [
    {"id": "O101", "customer": "Aarav", "items": ["Mouse", "Keyboard"], "status": "Delivered"},
    {"id": "O102", "customer": "Maya", "items": ["Monitor", "Mouse", "Keyboard"], "status": "Pending"},
    {"id": "O103", "customer": "Rohan", "items": ["Laptop", "Mouse"], "status": "Delivered"},
    {"id": "O104", "customer": "Neha", "items": ["Keyboard", "Mouse", "Webcam"], "status": "Cancelled"},
    {"id": "O105", "customer": "Kabir", "items": ["Laptop", "Keyboard"], "status": "Delivered"},
    {"id": "O106", "customer": "Ishaan", "items": ["Monitor", "Mouse"], "status": "Pending"}
]

def get_customer_details(orders):
    delivered_customers = []
    order_item_counts = {}
    pending_orders = []
    customer_item_totals = {}
    customers_with_mouse = []

    for order in orders:
        total_items = 0

        for item in order['items']:
            total_items += 1
            if item == 'Mouse' and order['customer'] not in customers_with_mouse:
                customers_with_mouse.append(order['customer'])

        if order['status'] == 'Delivered':
            delivered_customers.append(order['customer'])

        if order['status'] == 'Pending':
            pending_orders.append(order['id'])

        order_item_counts[order['id']] = total_items

        if order['customer'] not in customer_item_totals:
            customer_item_totals[order['customer']] = total_items
        else:
            customer_item_totals[order['customer']] += total_items

    return {
        'delivered_customers': delivered_customers,
        'order_item_counts': order_item_counts,
        'pending_orders': pending_orders,
        'customer_item_totals': customer_item_totals,
        'customers_with_mouse': customers_with_mouse
    }
print(get_customer_details(orders))