''' Write a function that returns the customer names whose total order amount is greater than or equal to amount_limit.
    test with amount_limit = 500.

    Requirements:

    Use .items() to iterate through orders.

    Use loops to calculate each order's total.

    Do not use sum(), len(), max(), or sorted().

    Do not use list comprehensions.

    Do not modify orders.

    Do not print inside the function.'''

orders = {
    "O101": {"customer": "Aarav", "items": ["laptop", "mouse"], "amounts": [1200, 25]},
    "O102": {"customer": "Maya", "items": ["chair"], "amounts": [150]},
    "O103": {"customer": "Rohan", "items": ["monitor", "keyboard"], "amounts": [450, 80]},
    "O104": {"customer": "Neha", "items": ["desk", "lamp"], "amounts": [300, 40]}
}

def get_customer_name(orders, amount_limit):

    customer_list = []
    for key,value in orders.items():
        total_amount = 0
        for amount in value['amounts']:
            total_amount += amount

        if total_amount >= amount_limit:
            customer_list.append(value['customer'])

    return customer_list

print(get_customer_name(orders, 500))