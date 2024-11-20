
# Prompt user for pizza toppings
while True:
    topping = input("Enter a topping to add to your pizza (or type 'exit' to finish): ")
    if topping.lower() == 'exit':
        break
    print(f"{topping.title()} will be added to your pizza!")
