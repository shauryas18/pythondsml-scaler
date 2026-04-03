while True:
    password = input("Enter password: ")
    if password == "admin123":
        print("Access Granted")
        break
    else:
        print("Wrong password, try again")