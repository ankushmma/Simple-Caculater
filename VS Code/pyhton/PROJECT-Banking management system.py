#Banking Management System
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, balance=0):
        self.accounts[account_number] = Account(account_number, name, balance)

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


def main():
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            bank.create_account(account_number, name)
            print("Account created successfully!")
        
        elif choice == 2:
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
                print(f"Deposited {amount} into account {account_number}")
            else:
                print("Account not found!")
        
        elif choice == 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
                print(f"Withdrew {amount} from account {account_number}")
            else:
                print("Account not found!")
        
        elif choice == 4:
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Balance: {account.get_balance()}")
            else:
                print("Account not found!")
        
        elif choice == 5:
            break
        
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
