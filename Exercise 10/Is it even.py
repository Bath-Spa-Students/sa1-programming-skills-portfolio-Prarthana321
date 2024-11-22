#This is the function to check whether the user input is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even." #Displays on the screen if the user input is even.
    else:
        return "The number is odd." #Displays on the screen if the user input is odd.

#This is the function to ask the user for input and stores it in the result and displays the result on screen.
def main():
    number = int(input("Enter a number: ")) 
    result = check_even_odd(number)  
    print(result)

#This function only runs when the script is exected directly.
if __name__ == "__main__":
    main()
    
