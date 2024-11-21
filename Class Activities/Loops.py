# Using Loops Instead of Multiple Print Statements
# Loops help avoid redundant code and improve efficiency.

# While Loop Example
# A while loop continues as long as the condition is True.
num = 1
while num < 10:
    print(num)
    num += 1  # Increment to prevent infinite loop

# While Loop with a Counter
counter = 1
while counter <= 5:
    print("Current Count:", counter)
    counter += 1

# Infinite Loop with Break
index = 1
while index < 6:
    print(index)
    if index == 3:  # Exit loop when `index` equals 3
        break
    index += 1

# For Loop Example
# Iterate through items in a sequence (list, tuple, or string).
vehicles = ["car", "bike", "truck"]
for vehicle in vehicles:
    print(vehicle)

# Using `range()` with a For Loop
# `range(start, stop, step)` generates a sequence of numbers.
for num in range(1, 15):  # Numbers from 1 to 14
    print(num)

for num in range(5):  # Numbers from 0 to 4
    print(num)

# Printing with Readability
for num in range(1, 15):
    print(num, end=", ")  # Print on the same line separated by commas

# Steps in `range()`
for num in range(1, 15, 3):  # Increment by 3
    print(num, end=", ")

for num in range(2, 20, 4):  # Increment by 4
    print(num, end=", ")

# Activity: Calculate Square Roots
import math
for val in range(1, 6):  # Values from 1 to 5
    print(f"Square root of {val}: {math.sqrt(val):.2f}")

# User Input with a For Loop
limit = int(input("Enter the range limit: "))
for num in range(limit + 1):
    print(num, end=", ")

# Summing Input Values
total_sum = 0
for _ in range(4):  # Loop to input 4 numbers
    number = float(input("Enter a number: "))
    total_sum += number
print("Sum of numbers:", total_sum)

# Sentinel-Controlled While Loop
total = 0
while True:
    number = float(input("Enter a value (-1 to stop): "))
    if number == -1:  # Exit loop when -1 is entered
        break
    total += number
print("Cumulative Total:", total)

# Nested Loops
# Example 1: Combination of Two Lists
set1 = ["A", "B", "C"]
set2 = [1, 2, 3]
for letter in set1:
    for digit in set2:
        print(letter, digit)

# Example 2: Nested Ranges
for outer in range(3):  # Outer loop (0, 1, 2)
    for inner in range(2):  # Inner loop (0, 1)
        print("Outer:", outer, "Inner:", inner)
