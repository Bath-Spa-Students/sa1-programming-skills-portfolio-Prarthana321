# Python Lists: Dynamic collections that support multiple data types.
# They can be homogeneous (same type) or heterogeneous (different types).

# Homogeneous List Example
colors = ["Red", "Blue", "Green"]
print(colors)

# Heterogeneous List Example
profile = ["John Doe", 25, True]
print(profile)

# Repetition Operator (*) for duplicating elements in a list
data = [1, 0, 1]
duplicated_data = data * 3
print(duplicated_data)

# Positive Indexing: Access list elements using non-negative integers
data = [10, 20, 30, 40, 50]
print(data[4])  # Access element at index 4

# Negative Indexing: Access list elements starting from -1
data = [10, 20, 30, 40, 50]
print(data[-1])  # Access the last element

# `len()`: Returns the total number of elements in a list
data = [5, 10, 15, 20]
print("Length of the list:", len(data))

# Lists are mutable, meaning their contents can be changed
data[2] = 99  # Updating the third element
print(data)

# Concatenation: Merging two lists using `+`
alpha = ["A", "B", "C"]
numeric = [1, 2, 3]
combined = alpha + numeric
print(combined)

# Slicing: Extracting a subset of a list
letters = ["a", "b", "c", "d", "e", "f"]
subset = letters[2:5]  # Extract elements from index 2 to 4
print(subset)

# `in` operator: Check if an element exists in a list
if "b" in letters:
    print("Found 'b'")
else:
    print("'b' not found")

# `not in` operator: Verify if an element is absent in a list
if "z" not in letters:
    print("'z' is not in the list")

# Built-in List Methods

# `append()`: Add an element at the end
letters.append("g")
print(letters)

# `index()`: Find the index of an element
print("Index of 'c':", letters.index("c"))

# `sort()`: Arrange elements in ascending order
numbers = [9, 3, 7, 2]
numbers.sort()
print("Sorted list:", numbers)

# `reverse()`: Reverse the order of the list
numbers.reverse()
print("Reversed list:", numbers)

# `remove()`: Delete the first occurrence of an element
numbers.remove(7)
print("After removal:", numbers)

# `max()` and `min()`: Retrieve the maximum and minimum values
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
