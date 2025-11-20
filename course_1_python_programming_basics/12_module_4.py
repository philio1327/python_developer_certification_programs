## Data Structures: Your Python Organization System
# Create a dictionary to store contact information
contacts = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9012"}

# Look up Bob's phone number
bobs_phone = contacts["Bob"]
print(bobs_phone)
# Output: 555-5678

# Add a new contact
contacts["David"] = "555-4321"

# Update Carol's phone number
contacts["Carol"] = "555-2468"

# Remove Alice's contact information
del contacts["Alice"]

# Print updated contacts
print(contacts)

# Example 2
# Create a set of favorite programming languages
languages = {"Python", "JavaScript", "Java"}
# Add "C++" to the set
languages.add("C++")
# Try to add "Python" again (it won't be added because it's a duplicate)
languages.add("Python")
print(languages)  # Output: {'Python', 'C++', 'JavaScript', 'Java'} (order may vary)
# Remove "Java"
languages.remove("Java")
# Create another set of languages
web_languages = {"JavaScript", "HTML", "CSS"}
# Find common languages between the two sets
common_languages = languages.intersection(web_languages)
print(common_languages)  # Output: {'JavaScript'}

# Example 3
# Values provided (do not change)
array = [1, 2, 2, 3, 1, 4, 5, 3]

# The following line will need to change to only store unique values
unique_set = set(array)

# List conversion and print provided (do not change)
unique_array = list(unique_set)
print(unique_array)