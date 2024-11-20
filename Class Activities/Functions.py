# Python functions simplify code by allowing reuse. 
# There are two main types of functions:
# 1. Void functions: Perform an action but do not return a value.
# 2. Value-returning functions: Take input, process it, and return a value.

# Function names should clearly indicate their purpose (e.g., `find_max`, `compute_sum`).
# Use the `def` keyword to define a function.
# Indentation is crucial within a function body.

# Example of a void function
def display_message():
    print("This is a void function!")

# Calling the void function
display_message()

# Local variable example
def display_message():
    text = "This is a local variable example!"  # `text` is only accessible within this function.
    print(text)

display_message()

# Uncommenting the next line will raise a NameError:
# print(text)

# Functions with identical local variable names do not interfere with each other
def func1():
    info = "Local to func1"
    print(info)

def func2():
    info = "Local to func2"
    print(info)

func1()
func2()

# Passing arguments to a function
def say_hello(greeting):  # `greeting` is a parameter.
    print(greeting)

msg = "Good Afternoon"
say_hello(msg)  # Passing `msg` as an argument.

# Function to calculate double of a given number
def main():
    number = 7
    calculate_double(number)

def calculate_double(value):
    print(value * 2)

main()

# Example of a function with multiple arguments
def student_info(name, grade):
    print(f"Student Name: {name}, Grade: {grade}")

student_info("Sophia", "A+")

# Refer to this link for more information:
# https://www.w3schools.com/python/python_functions.asp
