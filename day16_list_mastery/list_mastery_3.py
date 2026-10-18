'''
"unique_items" → each item appears once, preserving its first appearance order
"duplicate_items" → each duplicated item appears once, in the order it first becomes a duplicate
"item_count" → total number of items in the original list, counted manually with a loop.

Restrictions

Use loops and conditions.
No set(), len(), count(), sorted(), or list comprehensions.
Do not modify the original list.
No print() inside the function.
Return exactly these three keys.'''

items = ["pen", "book", "pen", "pencil", "book", "eraser", "pen", "ruler", "eraser", "marker"]

def analyze_items(items):
    unique_items = []
    duplicate_items = []
    item_count = 0

    for item in items:
        if item in unique_items and item not in duplicate_items:
            duplicate_items.append(item)

        if item not in unique_items:
            unique_items.append(item)

        

        item_count += 1
    return{

        'unique_items': unique_items,
        'duplicate_items': duplicate_items,
        'item_count': item_count
    }

print(analyze_items(items))