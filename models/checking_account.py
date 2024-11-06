from .bank_account import BankAccount
from .transaction import Transaction

class CheckingAccount(BankAccount):
    """A checking account that includes an overdraft facility."""
    def __init__(self, account_number, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft_fee = 35  # Fee for overdraft

    def withdraw(self, amount):
        """Withdraws amount with overdraft check and fee if needed."""
        if amount > 0 and (self.balance + self.overdraft_limit) >= amount:
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))

            # Apply overdraft fee if balance goes negative
            if self.balance < 0:
                self.balance -= self.overdraft_fee
                self.transactions.append(Transaction(self.overdraft_fee, "Overdraft Fee"))
        else:
            raise ValueError("Overdraft limit exceeded or invalid amount.")
