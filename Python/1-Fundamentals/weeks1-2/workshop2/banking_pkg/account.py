def show_balance(balance):
    '''
        Get users balance
    '''
    print("Your available balance is: ", float(balance))


def deposit(balance):
    '''
       Deposit money into account
    '''
    amount = input("Enter amount to deposit: ")
    balance = float(balance) + int(amount)
    return balance


def withdraw(balance):
    '''
        Take yo money back
    '''
    amount = input("Enter amount to withdraw: ")
    return float(balance) - int(amount)


def logout(name):
    '''
        Exit program
    '''
    print("Goodbye", name)
