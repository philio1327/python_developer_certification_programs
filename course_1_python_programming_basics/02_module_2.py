## Decisions and selections
order_total = 10
if order_total >= 50:
	print("Congratulations! You qualify for free shipping.")

# Introducing "else" statement
if order_total >= 50:
	print("Congratulations! You qualify for free shipping.")
else:
	print("Add more items to your cart to reach the free shipping threshold!")

# Introducing "elif" statement
points = 10_000
if points >= 1000:
	print("You've achieved Platinum status! Enjoy exclusive benefits.")
elif points >= 500:
	print("You're a Gold member! Thank you for your loyalty.")
elif points >= 100:
	print("Welcome to the Silver tier! Start earning rewards.")
else:
	print("You're a Bronze member. Keep shopping to earn more points!")

# Introduction to loops and conditional statements
valid_input = False
while not valid_input:
	user_input = int(input("Please enter a number greater than 0: "))
	if user_input > 0:
		valid_input = True
	else:
		print("Invalid input. Please try again.")

player_score = 80

if player_score > 100:
	print("Congratulations! You scored over 100 points.")
else:
	print("Keep trying to beat your high score!")

import random

secret_number = 4

guess = 0

while guess != secret_number:
	guess = random.randint(1, 10)
	print("Guessing:",guess)

print("I guessed the right number! It was", secret_number)

# Repeating actions
for i in range(1,11): # This loop prints 1 through 10, not through 11
    print(i)

number = 1
while number <= 10:
    print(number)
    number = number + 1

option = 0
while option != 4:
    print("1. Perform action 1")
    print("2. Perform action 2")
    print("3. Perform action 3")
    print("4. Quit")
    option = 4 # so we don't have infinite loop

fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]

fruits = ["apple", "banana", "cherry"]
fruit_length = len(fruits)
print(fruit_length)

fruits.append("date")
print(fruits)

# looping over elements
students = ["Alice", "Bob", "Charlie"]
for student in students:
    print("Hello,", student)

# looping over indices
students = ["Alice", "Bob", "Charlie"]
for i in range(0,len(students)):
    print("Hello,", students[i])

# rolling a die until we roll a 6

import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print("You rolled a", roll)

# calculate sum from 1 to 100 inclusive
total = 0
for number in range(1, 101):
    total += number
    print("The sum is:", total)

# extract all even numbers from the list
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1

# print multiplication tables
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j, end="\t") # Print the equation
    print() # Move to the next line after each row

# print all values that are divisible by 12 up to max_value (50 by default)
max_value = 50

for i in range(max_value+1):
    if i % 3 == 0 and i % 4 == 0:
        print(i)