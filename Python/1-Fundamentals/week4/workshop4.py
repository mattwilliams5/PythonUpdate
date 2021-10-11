class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your username has been changed to", self.name)
        return name

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to", self.pin)
        return pin

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "Has a balance of:", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.balance == 0:
            print("No funds available", self.balance)
        else:
            self.balance -= amount
        print(self.name, "Has a balance of:", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, transfer, amount):
        pin = self.pin

        if pin == self.pin:
            self.withdraw(amount)
            transfer.deposit(amount)

            print("Transfer Succesful")
            print(f"Tansferring ${amount: .2f} to {transfer.name}")
            return True
        else:
            return False

    def request_money(self, amount, requestor):
        if amount < 0:
            print("Please deposit a dollar or more")
            return False
        elif amount > requestor.balance:
            print(f"{requestor.name} is broke...Sorry")
            return False
        else:
            print(f"Requested ${amount: .2f} from {requestor.name}")


# """ Driver Code for Task 1 """
new_user = User("Matt", 1234, "password")
# print(new_user.name, new_user.pin, new_user.password)
# """ Driver Code for Task 2 """
# print(new_user.name, new_user.pin, new_user.password)
# new_user.change_name("Nancy")
# new_user.change_pin(4321)
# new_user.change_password("WordPass")
# print(new_user.name, new_user.pin, new_user.password)
# """ Driver Code for Task 3 """
new_user = BankUser("Matt", 1234, "password")
# print(new_user.name, new_user.pin, new_user.password, new_user.balance)
# # """ Driver Code for Task 4 """
# new_user.deposit(555)
# new_user.withdraw(55)

print(new_user.name, new_user.pin, new_user.password, new_user.balance)
# """ Driver Code for Task 5 """
new_user = BankUser("Tom", 1234, "password")
new_user2 = BankUser("Matt", 1234, "password")
new_user.deposit(5000)
print(new_user.name, new_user.pin, new_user.password, new_user.balance)
new_user2.transfer_money(new_user, 540)
print(new_user.name, new_user.pin, new_user.password,
      new_user.balance, new_user2.balance)
