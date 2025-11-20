## Write a function
def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        ValueError: If length or width are negative.
    """


    if not (isinstance(length, float) and isinstance(width, float)):
        raise TypeError("Input values must be numbers")
    if length < 0 or width < 0:
        raise ValueError("Input values must be positive numbers")
    return length * width

## Activity: Experimenting with built-in functions
# Part 1
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures)
lowest_temp = min(antarctic_temperatures)

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature
avg = sum(antarctic_temperatures) / len(antarctic_temperatures)
average_temp = round(avg, 1)
print("Average temperature:", average_temp, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp)
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")

# Part 2
int_value = 15
float_value = 4.1
text_value = "33"

type_of_float_value = type(float_value)

# Convert text_value to an integer
text_value_as_int = int(text_value)

# Convert int_value to text
int_value_as_text = str(int_value)

# DO NOT CHANGE LINES BELOW
# Print the type of float_value
print("float_value type:", type_of_float_value)

# Adding text_value_as_int to int_value
print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

# Adding (concatenating) text values
print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)