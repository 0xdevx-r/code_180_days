'''
Return:

all_categories → set of unique categories
category_customers → Category → set of customers
customer_products → Customer → tuple of products purchased, preserving order
product_customers → Product → set of customers
category_revenue → Category → total revenue
highest_revenue_customer → customer with highest revenue'''

sales = [
    ("Aarav", "Electronics", ("Laptop", "Mouse"), 76200),
    ("Maya", "Furniture", ("Chair", "Desk"), 20500),
    ("Rohan", "Electronics", ("Mouse", "Keyboard"), 3700),
    ("Neha", "Electronics", ("Laptop", "Monitor"), 93000),
    ("Kabir", "Furniture", ("Desk", "Chair"), 20500),
    ("Ishaan", "Electronics", ("Keyboard", "Mouse"), 3700)
]

def get_sales_data(sales):

    all_categories = set()
    category_customers = {}
    customer_products = {}
    product_customers = {}
    category_revenue = {}
    highest_revenue_customer = ''
    highest_revenue = float('-inf')

    for name, category, products, cost in sales:
        
        all_categories.add(category)
        
        if category not in category_customers:
            category_customers[category] = set()
        category_customers[category].add(name)

        if name not in customer_products:
            customer_products[name] = products

        for product in products:

            if product not in product_customers:
                product_customers[product] = set()

            product_customers[product].add(name)

        if category not in category_revenue:
            category_revenue[category] = 0

        category_revenue[category] += cost

        if cost > highest_revenue:
            highest_revenue = cost
            highest_revenue_customer = name
            
        
    return {
        'all_categories': all_categories,
        'category_customers':category_customers,
        'customer_products': customer_products,
        'product_customers':product_customers,
        'category_revenue': category_revenue,
        'highest_revenue_customer': highest_revenue_customer
        }

print(get_sales_data(sales))