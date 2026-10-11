'''Return exactly these keys:
  "low_stock" → product names where current stock is less than 5.
  "high_revenue" → product names whose revenue (price × total units sold) is at least revenue_limit.
  "best_seller" → product with the highest total units sold.
  "total_revenue" → revenue across all products.
  Test with revenue_limit = 1000.
  Requirements: Use .items(), 
  one outer loop an inner loop for sold 
  manual calculations
  no sum(), max(), sorted(), or list comprehensions
  Do not modify the data call previous functions, or print inside the function'''

inventory = {
  "laptop": {"price": 1200, "stock": 5, "sold": [2, 1, 3]},
  "mouse": {"price": 25, "stock": 12, "sold": [4, 2, 1]},
  "keyboard": {"price": 80, "stock": 3, "sold": [1, 2, 2]},
  "monitor": {"price": 450, "stock": 8, "sold": [2, 1, 1]},
  "webcam": {"price": 100, "stock": 4, "sold": [1, 1, 1]}
}

def get_stock_details(inventory, revenue_limit):
  
  low_stock = []
  high_revenue = []
  best_seller = ''
  total_revenue = 0
  highest_selling = float('-inf')

  for key,value in inventory.items():
    total_sold = 0

    if value['stock'] < 5:
      low_stock.append(key)
    
    for num in value['sold']:
      total_sold += num
    product_revenue = total_sold * value['price']

    if total_sold > highest_selling:
      highest_selling = total_sold
      best_seller = key

    if product_revenue >= revenue_limit:
      high_revenue.append(key)

    total_revenue += product_revenue
    
  return {
      "low_stock": low_stock,
      "high_revenue": high_revenue,
      "best_seller": best_seller,
      "total_revenue": total_revenue
    }
    
print(get_stock_details(inventory, 1000))