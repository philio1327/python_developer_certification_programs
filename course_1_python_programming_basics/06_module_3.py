## Variable Scope
# Example 1
def calculate_average(numbers):
    total = 0  # Local variable
    count = len(numbers)  # Local variable
    for num in numbers:
        total += num
    average = total / count
    return average

print(calculate_average([2, 5, 4, 1]))

# Example 2
# Global variable
COMPANY_NAME = "Global Tech Solutions"

def print_welcome_message():
    print("Welcome to", COMPANY_NAME.upper())

def print_contact_info():
    print("Contact", COMPANY_NAME, "at info@globaltechsolutions.com")

# Output: Welcome to GLOBAL TECH SOLUTIONS
print_welcome_message()

# Output: Contact Global Tech Solutions at info@globaltechsolutions.com
print_contact_info()

# Example 3
def outer_function():
    outer_var = "Hello from the outer function!"
    def inner_function():
        print(outer_var)  # Accessible from the enclosing scope
    inner_function()
outer_function()
# Two nested functions, the outer one labeled outer_function and the inner one inner_function
