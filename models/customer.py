import uuid

from models.bank_account import BankAccount


class Customer:
    def __init__(self, name):
        self.name = name
        self.customer_id = uuid.uuid4()
        self.accounts = {}

    def add_account(self, account_type:str, account:BankAccount):
        self.accounts[account_type] = account

    def get_account(self, account_type: str) -> BankAccount:
        return self.accounts.get(account_type)

    def get_account_statement(self, account_type: str):
        account = self.get_account(account_type)
        if account:
            print(f"Account Statement for {self.name}'s {account_type} Account:")
            for transaction in account.get_transaction_history():
                print(transaction)

        else:
            print(f"No {account_type} account found for {self.name}.")