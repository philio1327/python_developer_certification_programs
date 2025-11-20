# Create a list and add sample Celsius temperatures to it
celsius_temperatures = [] # Start with an empty list (do not modify)

# Add the Celsius temperatures to the list
celsius_temperatures += [0, 10, 25, 32, 100]

# Create an empty list to store Fahrenheit temperatures
fahrenheit_temperatures = []

# Print both lists - before adding to Fahrenheit list
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)

# Convert each Celsius temperature to Fahrenheit
for celsius in celsius_temperatures:  # Start the loop
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_temperatures.append(fahrenheit)  # Append to the list

# Print both lists - after adding to Fahrenheit list
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
