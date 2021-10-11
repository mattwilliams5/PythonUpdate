from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "admin"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as", authorized_user)

    choice = input("Please Enter Your Choice: ")
    if choice == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        authorized_user = (register(database, username))
        if authorized_user != "":
            database[username] = password
            print("User:", username, "Has been registered")
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation = donate(authorized_user)
            str(donation)
            donations.append(donation)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Thank you...Goodbye")
        break
