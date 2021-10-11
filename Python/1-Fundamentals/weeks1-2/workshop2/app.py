from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("")
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print("User: " + name)
print("Balace: " + str(balance))
print("------------------------------------------")
print("| 1.    Balance     | 2.    Deposit      |")
print("------------------------------------------")
print("------------------------------------------")
print("| 3.    Withdraw    | 4.    Logout       |")
print("------------------------------------------")

while True:
    name_to_validate = input("Please Login: ")
    pin_to_validate = input("Please enter your PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout
        break
