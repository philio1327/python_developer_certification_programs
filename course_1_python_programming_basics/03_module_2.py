## Control flow in Python
temperature = 22  # Example temperature

if temperature < 20:
    print("It might be cold! You might need a jacket.")
else:
    print("It's warm! Enjoy the sunshine.")

temperature = 15  # Let's assume the temperature is 15 degrees Celsius

if temperature < 10:
    print("Wear a jacket! It's cold out there.")
elif 10 <= temperature < 20:
    print("A light sweater should be fine. It's a bit chilly.")
elif 20 <= temperature < 30:
    print("Enjoy the pleasant weather! No need for extra layers.")
else:
    print("It's hot! Stay hydrated and wear sunscreen.")

# Automating repetition
# Example: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# indefinite iteration
# Example: Keep asking for input until the user enters "quit"
user_input = ""
while user_input != "quit":
    user_input = input("Enter something (or 'quit' to exit): ")
    print("You entered:", user_input)

# Coding exercise: Print whether list numbers are even or odd
numbers = [3, 9, 1, 10, 5, 2, 8]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")