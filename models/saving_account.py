from .bank_account import BankAccount
from .transaction import Transaction


class SavingsAccount(BankAccount):
    """A savings account that includes interest calculation."""

    def __init__(self, account_number, balance=0.0, interest_rate=0.01):
        super(SavingsAccount, self).__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Applies interest to the balance."""
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self.transactions.append(Transaction(interest, "Interest"))