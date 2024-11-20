# Get sales input from the user
revenue = int(input("Enter Revenue: "))

# Initialize bonus variable
extra = 0

# Check revenue condition
if revenue > 50000:
    extra = 500  # Assign bonus if condition is met
else:
    extra = 0  # No bonus for revenue <= 50000

# Display the calculated bonus
print("Your Extra Pay is " + str(extra))
