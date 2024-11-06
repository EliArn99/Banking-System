from interfaces.transaction_handler import TransactionHandler
from interfaces.balance_manager import BalanceManager
from models.transaction import Transaction

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []  # Initialize an empty list to store transactions

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, 'Deposit'))  # Corrected to transactions
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))  # Corrected to transactions
        else:
            raise ValueError("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return [str(transaction) for transaction in self.transactions]
