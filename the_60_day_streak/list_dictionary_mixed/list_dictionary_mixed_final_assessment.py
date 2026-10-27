'''
Return:
order_totals → Order ID → total price of all items
customer_spending → Customer → total amount spent
category_totals → Category → total revenue
customers_with_mouse → customers whose order contains "Mouse", original order
highest_spending_customer → customer with the highest total spending
product_counts → Product → number of times it appears across all orders

Restrictions: No len(), count(), sum(), max(), min(), sorted(), set(), or comprehensions.
No mutation of orders; no print() inside the function'''

orders = [
    {
        "id": "O101",
        "customer": "Aarav",
        "items": [
            {"name": "Mouse", "category": "Electronics", "price": 1200},
            {"name": "Keyboard", "category": "Electronics", "price": 2500}
        ]
    },
    {
        "id": "O102",
        "customer": "Maya",
        "items": [
            {"name": "Monitor", "category": "Electronics", "price": 18000},
            {"name": "Mouse", "category": "Electronics", "price": 1200},
            {"name": "Chair", "category": "Furniture", "price": 8500}
        ]
    },
    {
        "id": "O103",
        "customer": "Rohan",
        "items": [
            {"name": "Laptop", "category": "Electronics", "price": 75000},
            {"name": "Mouse", "category": "Electronics", "price": 1200}
        ]
    },
    {
        "id": "O104",
        "customer": "Neha",
        "items": [
            {"name": "Desk", "category": "Furniture", "price": 12000},
            {"name": "Chair", "category": "Furniture", "price": 8500},
            {"name": "Keyboard", "category": "Electronics", "price": 2500}
        ]
    },
    {
        "id": "O105",
        "customer": "Kabir",
        "items": [
            {"name": "Laptop", "category": "Electronics", "price": 75000}
        ]
    }
]

def get_customer_data(orders):

    order_totals = {}
    customer_spending = {}
    category_totals = {}
    customers_with_mouse = []
    highest_spending_customer = ''
    highest_spent = float('-inf')
    product_counts = {}

    for order in orders:
        total_cost = 0

        for item in order['items']:
            total_cost += item['price']

            if item['category'] not in category_totals:
                category_totals[item['category']] = item['price']
            else:
                category_totals[item['category']] += item['price']

            if item['name'] == 'Mouse' and order['customer'] not in customers_with_mouse:
                customers_with_mouse.append(order['customer'])

            if item['name'] not in product_counts:
                product_counts[item['name']] = 1
            else:
                 product_counts[item['name']] += 1

        order_totals[order['id']] = total_cost

        if order['customer'] not in customer_spending:
            customer_spending[order['customer']] = total_cost
        else:
            customer_spending[order['customer']] += total_cost
        
        if total_cost > highest_spent:
            highest_spent = total_cost
            highest_spending_customer = order['customer']

    return {

        'customer_spending': customer_spending,
        'order_totals': order_totals,
        'category_totals': category_totals,
        'customers_with_mouse': customers_with_mouse,
        'highest_spending_customer': highest_spending_customer,
        'product_counts': product_counts

    }
print(get_customer_data(orders))