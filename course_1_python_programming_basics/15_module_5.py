## Common Python exceptions

# NameError
def myfunction():
    local_var = 10
print(local_var) # NameError: name 'local_var' is not defined

# TypeError
def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers.")
    return length * width

print(calculate_area(5, 'three')) # TypeError: Length and width must be numbers.

# IndexError
my_list = [1, 2, 3]
for i in range(len(my_list)):
    print(my_list[i])

# Can encapsulate in a try-except block
my_list = []
try:
    print(my_list[0])
except IndexError:
    print("The list is empty.")

# KeyError
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Key not found in dictionary.")

import logging

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    logging.error(f"KeyError encountered: {e}")
    # Handle the error or provide a fallback mechanism

# Assignment
def get_city_population(populations, city):
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f'City "{city}" not found in population data.')