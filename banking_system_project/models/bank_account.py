from ..interfaces.transaction_handler import TransactionHandler
from ..interfaces.balance_manager import BalanceManager
from .transaction import Transaction

class BankAccount(TransactionHandler, BalanceManager):
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, "Deposit"))
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))
        else:
            raise ValueError("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return [str(transaction) for transaction in self.transactions]
