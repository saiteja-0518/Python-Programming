class Error(Exception):
    pass


class InSufficientBalanceError(Error):
    pass


class NegativeAmountDepositError(Error):
    pass


class NegativeWithDrawalError(Error):
    pass


class BankAccount:
    Bank_Name = "Sai Teja Bank"

    def __init__(self):
        self.account_number = None
        self.account_holder = None
        self.balance = 0.0

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial amount must be zero or above.")

        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def credit(self, amount):
        if amount <= 0:
            raise NegativeAmountDepositError("Enter a valid amount for deposit.")
        self.balance += amount

    def debit(self, amount):
        if amount <= 0:
            raise NegativeWithDrawalError("Enter a valid amount for withdrawal.")

        if amount > self.balance:
            raise InSufficientBalanceError("Insufficient balance.")

        self.balance -= amount

    def display_balance(self):
        print("Account Number :", self.account_number)
        print("Account Holder :", self.account_holder)
        print("Balance :", self.balance)