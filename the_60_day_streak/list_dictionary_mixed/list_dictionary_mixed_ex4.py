'''
Return:
product_quantities → Product → individual sale revenue (quantity × price)
category_quantities → Category → total quantity sold
total_revenue → total revenue across all sales
high_value_products → products whose individual sale revenue (quantity × price) is ≥ 20000, original order
top_revenue_product → product with the highest individual sale revenue

Restrictions
No:
len(), count(), sum(), max(), min(), sorted(), set(), comprehensions, mutation of orders
print() inside the function'''

sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 75000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 1200},
    {"product": "Chair", "category": "Furniture", "quantity": 3, "price": 8500},
    {"product": "Keyboard", "category": "Electronics", "quantity": 4, "price": 2500},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 12000},
    {"product": "Monitor", "category": "Electronics", "quantity": 3, "price": 18000}
]

def get_sales_data(sales):
    product_quantities = {}
    category_quantities = {}
    total_revenue = {}
    high_value_products = []
    top_revenue_product = ''
    highest_selling_price = float('-inf')

    for sale in sales:

        if sale['product'] not in product_quantities:
            product_quantities[sale['product']] = sale['quantity']
        else:
            product_quantities[sale['product']] += sale['quantity']

        if sale['category'] not in category_quantities:
            category_quantities[sale['category']] = sale['quantity']
        else:
            category_quantities[sale['category']] += sale['quantity']
        
        revenue = sale['quantity']*sale['price']
        total_revenue[sale['product']] = revenue

        if revenue >= 20000:
            high_value_products.append(sale['product'])

        if revenue > highest_selling_price:
            highest_selling_price = revenue
            top_revenue_product = sale['product']

    return{
        'category_quantities': category_quantities,
        'product_quantities': product_quantities,
        'total_revenue': total_revenue,
        'high_value_products': high_value_products,
        'top_revenue_product': top_revenue_product
        }

print(get_sales_data(sales))