
'''Return exactly
"large_orders" → customer names whose total order amount is >= amount_limit
"highest_order_customer" → customer with the highest total order amount
"total_sales" → total amount across all orders
Constraints:
- Use .items()
- One outer for loop
- Inner loop for amounts allowed
- Calculate totals manually
- Manually track highest order
- No sum(), max(), sorted(), list comprehensions
- No previous functions
- Don't modify orders
- No print() inside function
- Exactly three return keys'''

orders = {
    "O101": {
        "customer": "Aarav",
        "items": ["laptop", "mouse"],
        "amounts": [1200, 25]
    },
    "O102": {
        "customer": "Maya",
        "items": ["chair", "desk"],
        "amounts": [150, 300]
    },
    "O103": {
        "customer": "Rohan",
        "items": ["monitor", "keyboard"],
        "amounts": [450, 80]
    },
    "O104": {
        "customer": "Neha",
        "items": ["laptop", "webcam"],
        "amounts": [1200, 100]
    },
    "O105": {
        "customer": "Kabir",
        "items": ["desk", "chair"],
        "amounts": [300, 150]
    }
}

def get_customer_details(orders, amount_limit):
    large_orders = []
    highest_order_customer = ''
    total_sales = 0
    highest_order_amount = float('-inf')
    
    for key,value in orders.items():
        total_order_amount = 0

        for amount in value['amounts']:
            total_order_amount += amount
            total_sales += amount

        if total_order_amount >= amount_limit:
            large_orders.append(value['customer'])

        if total_order_amount > highest_order_amount:
            highest_order_amount = total_order_amount
            highest_order_customer = value['customer']

    return {

        "large_orders" : large_orders,
        "highest_order_customer": highest_order_customer,
        "total_sales": total_sales
    }

print(get_customer_details(orders, 500))