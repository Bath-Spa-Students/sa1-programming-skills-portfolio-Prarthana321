#Code to initialize list of names.
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Code to input a search term.
user_search_term = input("Enter a name to search: ")

#Code to Check if the user-provided name is in the list and print the result 
if user_search_term in names:
    print(f"'{user_search_term}' was found in the list.")
else:
    print(f"'{user_search_term}' was not found in the list.")
