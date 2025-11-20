## Common debugging strategies used by experienced developers
def calculatediscount(price, percentage):
	if percentage < 0 or percentage > 100:
		return "Invalid discount percentage" # Incorrect behavior
	discountamount = price * (percentage / 100)
	return price - discountamount
print(calculatediscount(100, 150)) # Should be an error

def calculate_discount(price, percentage):
	if percentage < 0 or percentage > 100:
		raise ValueError("Discount percentage must be between 0 and 100")
	discount_amount = price * (percentage / 100)
	return price - discount_amount
try:
	print(calculate_discount(100, 150))
except ValueError as e:
	print(f"Error: {e}")

import logging
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
def divide(x, y):
    try:
        result = x / y
        logging.info(f"Successfully divided {x} by {y} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted!")
        return None
divide(10, 2)
divide(5, 0)

# Example Assignment
def calculate_discount(price, discount_percentage):
  discount_amount = price * (discount_percentage / 100)
  discounted_price = price - discount_amount
  return discounted_price


# Code to test your output
price = 50
discount_percentage = 20
discounted_price = calculate_discount(price, discount_percentage)
print(discounted_price)