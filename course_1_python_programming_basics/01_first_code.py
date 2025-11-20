## VERY FIRST PROGRAM IN CERTIFICATION COURSE! Aug 15th, 2025
print("Hello World!")

## SECOND PROGRAM

length = 5
width = 3

# Calculate the area
area = length * width

# Print the result
print("The area of the rectangle is:", area)

## THIRD PROGRAM - The Power of Python
grade = "B"
# With if statements, the portion inside the block must be indented
if grade == "A":
    print("Excellent work!")
else:
    print("Keep studying and you'll improve!")

## FOURTH PROGRAM - Anatomy of a Python program
age = 25
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")

discount = 0.2  # 20% discount
price = 50
final_price = price * (1 - discount)
print(final_price)

import csv

# Read a CSV file - NOTE data.csv doesn't exist so this doesn't have anything to read
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

original_price = 75
discount_rate = 15

discount = (discount_rate / 100) * original_price
final_price = original_price - discount

print("The final price after discount is: $", final_price)



