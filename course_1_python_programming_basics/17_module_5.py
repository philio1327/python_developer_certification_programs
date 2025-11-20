## Exception handling best practices
# FileNotFoundError example
file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found -", file_name)

# ZeroDivisionError example
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except TypeError:
    print("Error: Invalid data types")

# logging
import logging

try:
    # Your potentially error-prone code here
except Exception as e:
    logging.error(f"An error occurred: {e}")  # Logs the exception with details

# Raising custom exceptions
class InvalidCredentialsError(Exception):
    pass

# ... later in your code ...
if not valid_credentials(username, password):
    raise InvalidCredentialsError("Incorrect username or password")

# Overly broad except clauses
try:
    result = some_function()  # This function might raise various exceptions
except:
    print("An error occurred")  # Hides the actual problem

# duck typing in Python
def calculate_area(shape):
    try:
        return shape.calculate_area()
    except AttributeError:
        raise TypeError("Object does not have a calculate_area_method")
