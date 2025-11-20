# Example 1 - Default values
def calculate_area(width=1, height=1):
    area = width * height
    return area

# Example 2 - Adding default value makes that parameter optional
def greet(name, greeting="Hello"):
    print(greeting, name) # name is mandatory, greeting argument is optional

greet("Alice")
greet("Carol", "Howdy")

# Example 3 - *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)

# Example 4 - Comprehensive example
def create_user_profile(name, age, occupation="Student", interests=None): # Use None as default
    """
    Creates a user profile with optional interests.

    Args:
        name (str): The user's name (required).
        age (int): The user's age (required).
        occupation (str, optional): The user's occupation (defaults to "Student").
        interests (list, optional): A list of the user's interests (defaults to None).
    """
    if interests is None:  # Initialize if None
        interests = []

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }

    return profile

# Usage
user1 = create_user_profile("Alice", 25, "Software Engineer", ["Coding", "Hiking"])
user2 = create_user_profile("Bob", 18)  # Uses default occupation and no interests
user3 = create_user_profile("Carol", 30, interests=["Gardening", "Reading"])

print(user1)
print(user2)
print(user3)

# Example 5 - Make a sandwich assignment solution
def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    return_string = f"Making a {'toasted ' if toasted else ''}{bread_type} sandwich with {filling}"
    if cheese:
        return_string += f" and {cheese} cheese."
    else:
        return_string += "."
    return return_string