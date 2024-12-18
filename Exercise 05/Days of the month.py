# Code to define the days in each month (default for non-leap years)
days_in_month = {
    1: 30,   #Month=January
    2: 28,   #Month=February
    3: 31,   #Month=March
    4: 30,   #Month=April
    5: 31,   #Month=May
    6: 30,   #Month=June 
    7: 31,   #Month=July
    8: 31,   #Month=August
    9: 30,   #Month=September
    10: 31,  #Month=October
    11: 30,  #Month=November
    12: 31   #Month=December
}

# Function to get the number of days in a specific month
try:
    # Asking the user to input the month number
    month = int(input("Enter the month number (1-12): "))
    
    # Validating the month number
    if month < 1 or month > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
        exit()
    # Checking if the month is February and handle leap year
    if month == 2:
        # Asking if it's a leap year
        leap_year = input("Is it a leap year? (yes or no): ").strip().lower()
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days in a non-leap year.")
    else:
        # Code to output the number of days for the selected month
        print(f"The month {month} has {days_in_month[month]} days.")

except ValueError:
    print("Invalid input. Please enter a number.")
