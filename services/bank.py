from models.customer import Customer
from models.bank_account import BankAccount
from models.transaction import Transaction

class Bank:
    def __init__(self, name):
        self.name = name
        self.customer = {}

    def add_customer(self, customer: Customer):
        self.customer[customer.customer_id] = customer

    def transfer(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        if from_account.get_balance() >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            from_account.transactions.append(Transaction(amount, "Transfer", f"To {to_account.account_number}"))  # Corrected
            to_account.transactions.append(Transaction(amount, "Transfer", f"From {from_account.account_number}"))  # Corrected
        else:
            raise ValueError("Insufficient funds for transfer")

    def find_customer_by_id(self, customer_id):
        return self.customer.get(customer_id)
