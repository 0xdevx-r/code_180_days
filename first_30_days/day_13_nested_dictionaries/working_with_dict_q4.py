'''Requirements
    expensive_products → product names where price > price_limit
    low_stock_products → product names where stock <= stock_limit
    expensive_count → number of expensive products
    highest_stock → product name with the highest stock
    Use .items()
    Use one for loop
    Do not use max(), min(), sorted(), or len()
    Do not modify products
    Do not call previous functions
    Do not print inside the function
    Exact dictionary keys matter'''

products = {
    "laptop": {"price": 1200, "stock": 5, "category": "electronics"},
    "mouse": {"price": 25, "stock": 12, "category": "electronics"},
    "desk": {"price": 300, "stock": 3, "category": "furniture"},
    "chair": {"price": 150, "stock": 8, "category": "furniture"},
    "monitor": {"price": 450, "stock": 2, "category": "electronics"}
}

def get_stock_details(products, price_limit, stock_limit):

    expensive_products = []
    low_stock_products = []
    expensive_count = 0
    highest_stock = ""
    highest_stock_item = float('-inf')

    for key,value in products.items():
        if value['price'] > price_limit:
            expensive_products.append(key)
            expensive_count += 1
            
        if value['stock'] <= stock_limit:
            low_stock_products.append(key)
            
        if value['stock'] > highest_stock_item:
            highest_stock_item = value['stock']
            highest_stock = key
            
    return {

        "expensive_products": expensive_products,
        "low_stock_products": low_stock_products,
        "expensive_count": expensive_count,
        "highest_stock": highest_stock

    }

print(get_stock_details(products, 200, 5))