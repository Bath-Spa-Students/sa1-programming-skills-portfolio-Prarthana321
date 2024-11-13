#Code to Define the correct password.
correct_password=12345

#Code to set the maximum number of attempts.
max_attempts=5

#Code to initialize the attempt counter to 0.
attempts_counter=0

#Code to start the loop to ask for the password.
while attempts_counter<max_attempts:
    enter_password=(int(input("Enter the password:"))) #Asking the user to input the password.
    #Code to check whether the entered password is correct.
    if enter_password==correct_password:
        print("Access Granted")
        break

    else:
        attempts_counter += 1 #Increments the attempt counter after every wrong attempt.

    #Code to calculate remaining attempts.
    remaining_attempts=max_attempts-attempts_counter

    #Code to feedback on remaining attempts.
    if remaining_attempts>0:
        print(f"Incorrect password. You have {remaining_attempts} attempts left")
    else:
        print("Maximum attempts reached. The authorities have been alerted.")