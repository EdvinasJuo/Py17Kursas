class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

def create_bank_account(account_number, owner, initial_balance=0):
    return BankAccount(account_number, owner, initial_balance)

def get_account_balance(account):
    return account.balance

def make_transaction(account, transaction_type, amount):
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        account.withdraw(amount)
    else:
        raise ValueError("Invalid transaction type.")