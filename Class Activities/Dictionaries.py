# Dictionaries in Python store data as key-value pairs.
# Keys must be immutable, while the values associated with them are mutable.
# Dictionaries are enclosed in curly braces `{}`.
# Use `in` and `not in` to check if a key exists in a dictionary.
# The `len()` function works for dictionaries, lists, and tuples.

# Initializing an empty dictionary
inventory = {}
print(inventory)

# Checking the type of the dictionary
inventory = {}
print(inventory, type(inventory))

# Alternative way to initialize a dictionary using `dict()`
inventory = dict()
print(inventory, type(inventory))

# Creating a dictionary with predefined key-value pairs
config = {'server': 'localhost', 'port': 8080, 'secure': True}
print(config)

# Adding values to a dictionary
user = {'Name': 'Sophia', 'Age': 25, 'Location': 'New York'}
print(user, type(user))
# Keys like 'Name', 'Age', and 'Location' are associated with their respective values.

# Accessing values using keys
print(user["Name"], type(user))

# Accessing a non-existent key raises a KeyError
# Uncommenting the next line will throw an error:
# print(user["Email"])

# Using the `get()` method to handle missing keys gracefully
print(user.get("Email"))

# Providing a default value with `get()` for missing keys
print(user.get("Email", "Not provided"))

# Using `.items()` to get all key-value pairs as tuples
print(user.items())

# Retrieving all keys from a dictionary
print(user.keys())

# Deleting a key-value pair using `del`
del user["Age"]
print(user.items())

# Using `pop()` to remove a key-value pair and return its value
age = user.pop("Name")
print(age)
print(user.keys())
print(user.values())

# Using `popitem()` to remove and return the last inserted key-value pair as a tuple
last_removed = user.popitem()
print(last_removed)
print(user.keys())
print(user.values())

# Looping through a dictionary with a for loop
options = {'quality': 'high', 'format': 'mp4', 'resolution': '1080p'}
for key, value in options.items():
    print(f"{key}: {value}")
