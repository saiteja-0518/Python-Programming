from saiteja_bank import *

account = BankAccount()

account_number = int(input("Enter account number : "))
account_holder = input("Enter account holder name : ")
initial_balance = float(input("Enter account initial balance : "))

try:
    account.create_account(account_number, account_holder, initial_balance)
except ValueError as e:
    print(e)
else:
    print("\nAccount Details")
    account.display_balance()
finally:
    print("Transaction process completed")

credit_amount = float(input("\nEnter amount to credit : "))

try:
    account.credit(credit_amount)
except NegativeAmountDepositError as e:
    print(e)
else:
    print("Credit successful")
    account.display_balance()
finally:
    print("Transaction process completed")

debit_amount = float(input("\nEnter amount to debit : "))

try:
    account.debit(debit_amount)
except NegativeWithDrawalError as e:
    print(e)
except InSufficientBalanceError as e:
    print(e)
else:
    print("Debit successful")
    account.display_balance()
finally:
    print("Transaction process completed")

print("\nTrying to debit 8000")

try:
    account.debit(8000)
except InSufficientBalanceError as e:
    print(e)
except NegativeWithDrawalError as e:
    print(e)
finally:
    print("Transaction process completed")

print("\nTrying to credit -500")

try:
    account.credit(-500)
except NegativeAmountDepositError as e:
    print(e)
finally:
    print("Transaction process completed")

print("\nCurrent Balance :", account.balance)