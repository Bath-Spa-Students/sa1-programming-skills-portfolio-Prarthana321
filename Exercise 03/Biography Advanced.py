#Code to input user's first name.
user_firstname=str(input("Enter your first name: "))

#Code to input user's second name.
user_secondname=str(input("Enter your second name: "))

#Code to input user's hometown.
user_hometown=str(input("Enter your hometown: "))

#Code to input user's age.
while True:
    try:
        user_age=int(input("Enter your age:"))
        break
    except ValueError:
        print("Invalid input for age. Enter the number.")

#Code to store the information in dictionary.
information= {
    "First name": user_firstname,
    "Second name": user_secondname,
    "Hometown": user_hometown,
    "Age": user_age
}

#Code to print values
print(f"FIRST NAME: {information['First name']}\nSECOND NAME: {information['Second name']}\nHOMETOWN: {information['Hometown']}\nAGE: {information['Age']}")
