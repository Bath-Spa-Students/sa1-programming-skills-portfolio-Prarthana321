dict_months={
    1:31, #Month=January.
    2:28, #Month=February.
    3:31, #Month=March.
    4:30, #Month=April.
    5:31, #Month=May.
    6:30, #Month=June.
    7:31, #Month=July.
    8:31, #Month=August.
    9:30, #Month=September.
    10:31, #Month=October.
    11:30, #Month=November.
    12:31 #Month=December.
    }
#Code to ask the user to input the month number.
user_input=int(input("Enter the month number:"))
#Code to check whether the input is valid.
if user_input in dict_months:
    #Advanced Requirement(To ask the user whether february is leap year.)
    if dict_months==2:
        leap_year=input("Is february leap year? Answer in yes or no:")
        #Code to adjust february as leap year.
        if leap_year=="yes":
            print("The number of days in February (leap year) is 29.")
        else:
            print("The number of days in February is 28")
    else:
        print(f"The number of days in month {user_input} is {dict_months[user_input]}")
else:
    print(f"Invalid number.Enter number between 1-12.")



