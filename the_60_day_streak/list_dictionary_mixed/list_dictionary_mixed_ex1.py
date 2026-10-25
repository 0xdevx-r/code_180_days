'''
Return:
electronics
Product names belonging to "Electronics"
Preserve original order.

price_by_id
Dictionary mapping product ID → price.

category_counts
Dictionary mapping category → number of products.

expensive_products
Product names with price >= 5000.
Preserve original order.

total_price
Total price of all products.
Calculate manually.

Restrictions
No:
len()
count()
sum()
max()
min()
sorted()
set()
comprehensions
mutation of products
print() inside the function'''

products = [
   {"id": "P101", "name": "Laptop", "category": "Electronics", "price": 75000},
   {"id": "P102", "name": "Mouse", "category": "Electronics", "price": 1200},
   {"id": "P103", "name": "Office Chair", "category": "Furniture", "price": 8500},
   {"id": "P104", "name": "Keyboard", "category": "Electronics", "price": 2500},
   {"id": "P105", "name": "Desk", "category": "Furniture", "price": 12000}
]

def get_product_details(products):
   electronics = []
   price_by_id = {}
   category_counts = {}
   expensive_products = []
   total_price = 0
   

   for product in products:
      
      if product['category'] == 'Electronics':
         electronics.append(product['name'])

      price_by_id[product['id']] = product['price']

      if product['category'] not in category_counts:
         category_counts[product['category']] = 1
      else:
         category_counts[product['category']] += 1

      if product['price'] >= 5000:
         expensive_products.append(product['name'])

      total_price += product['price']
      

   return {'electronics': electronics,
           'price_by_id': price_by_id,
           'category_counts': category_counts,
           'expensive_products': expensive_products,
           'total_price': total_price
           }
print(get_product_details(products))