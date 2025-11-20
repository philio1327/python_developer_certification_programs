## Example 1
shopping_list = ["apples", "bananas", "milk"]  # List for items
item_quantities = {"apples": 3, "bananas": 1}  # Dictionary for quantities

# User adds an item
shopping_list.append("eggs")
item_quantities["eggs"] = 12

# User increases the quantity of bananas
item_quantities["bananas"] += 2

# User removes apples
shopping_list.remove("apples")
del item_quantities["apples"]

# Print updated list and dictionary
print(shopping_list)
print(item_quantities)

## Example 2
# Tuples
coordinates = (37.7749, -122.4194)  # Latitude, longitude of San Francisco
birth_date = (1990, 12, 25)       # Year, month, day

# Sets
unique_colors = {"red", "green", "blue"}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)    # Removes duplicates

## Example 3 - Task
# Create an empty list to represent the shopping cart
shopping_cart = []

# Add items to the shopping cart
shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")

# Print the contents of the shopping cart
print()
print("Shopping Cart:")
for item in shopping_cart:
    print(item)

## Real-world applications example
# Add the SKU data provided to the product catalog dictionary
product_catalog = {}
product_catalog["SKU123"] = {"name": "Widget A", "price": 19.99, "quantity": 50}
product_catalog["SKU456"] = {"name": "Gadget B", "price": 34.95, "quantity": 25}
product_catalog["SKU789"] = {"name": "Gizmo C", "price": 9.99, "quantity": 100}

# Look up this SKU in your code.
sku_to_find = "SKU123"
price = product_catalog[sku_to_find]["price"]
print(f"The price of {product_catalog[sku_to_find]['name']} is ${price}")