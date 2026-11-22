''' 
Return
unique_products → set of all unique products
customer_products → Customer → set of products purchased
product_customers → Product → set of customers who purchased it
customers_with_mouse → set of customers who purchased Mouse
order_product_counts → Order ID → number of product entries, including duplicates'''

orders = [
    ("O101", "Aarav", ("Mouse", "Keyboard", "Mouse")),
    ("O102", "Maya", ("Monitor", "Mouse")),
    ("O103", "Rohan", ("Laptop", "Keyboard")),
    ("O104", "Neha", ("Mouse", "Webcam", "Keyboard")),
    ("O105", "Kabir", ("Monitor", "Webcam")),
    ("O106", "Ishaan", ("Laptop", "Mouse", "Monitor"))
]

def get_product_data(orders):
    unique_products = set()
    customer_products = {}
    product_customers = {}
    customers_with_mouse = set()
    order_product_counts = {}

    for order_id, name, products in orders:
        product_count = 0
        customer_products[name] = set(products)

        for product in products:
            unique_products.add(product)
            product_count += 1
        
            if product not in product_customers:
                product_customers[product] = set()

            product_customers[product].add(name)
        
        order_product_counts[order_id] = product_count

        if 'Mouse' in products:
            customers_with_mouse.add(name)

    return{'unique_products': unique_products,
           'customer_products': customer_products,
           'product_customers': product_customers,
           'customers_with_mouse': customers_with_mouse,
           'order_product_counts': order_product_counts
        } 

print(get_product_data(orders))
