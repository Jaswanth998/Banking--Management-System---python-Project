# ----------- BANKING SYSTEM -------------

class Account:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"\nAmount Deposited: {amount}")
        print(f"Total Balance: {self.balance}")

    # Withdraw money
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nAmount Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    # Get current balance
    def get_balance(self):
        return self.balance

    # Mini statement
    def get_mini_statement(self):
        print("\n----- MINI STATEMENT -----")
        print(f"Username        : {self.username}")
        print(f"Current Balance : {self.balance}")
        print("--------------------------")


class BankingSystem:
    def __init__(self):
        self.accounts = {}  # Stores accounts in dictionary (username -> Account object)

    # Create a new account
    def create_account(self, username, password):
        if username in self.accounts:
            print("Username already exists. Please choose another one.")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully!")
            print("------- Welcome to PYTHON Bank -------")

    # Login to account
    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Successful...")
                return account
            else:
                print("Invalid password!")
        else:
            print("Invalid username!")
        return None


# ------------ MAIN PROGRAM ------------

bank = BankingSystem()

while True:
    print("\n========== JASWANTH BANK ==========")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username, password)

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        account = bank.login(username, password)

        if account is not None:
            while True:
                print("\n----- Welcome to JASWANTH Bank -----")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Logout")
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif choice == '2':
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif choice == '3':
                    print(f"Current Balance: {account.get_balance()}")

                elif choice == '4':
                    account.get_mini_statement()

                elif choice == '5':
                    print("\n-------- THANK YOU, VISIT AGAIN --------")
                    break
                else:
                    print("Invalid choice. Try again!")

    elif choice == '3':
        print("\n------ THANK YOU ------")
        break

    else:
        print("Invalid choice. Try again!")

# ----------- FINISHED ------- THANK YOU ---------
