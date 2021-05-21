import details

# MISSING COMPLETE ERROR HANDLING, THAT IS SOMETHING I WILL HAVE TO ADD


# This is where the primary logic will be kept

def main_loop():
    decision = int(input("1: Get Password\n2: Make Password\nChoose what you would like to do: "))

    # Fetch a password based on name
    if decision == 1:
        password_name = input("What is the password for?: ")
        print(details.Password.fetch_password(password_name),"\n")
        main_loop()

    if decision == 2:
        new_password = details.Password.create_new_password()
        new_password.save_password()
        main_loop()

if __name__ == "__main__":
    print('WELCOME TO THE PASSWORD MANAGER \n')
    main_loop()
