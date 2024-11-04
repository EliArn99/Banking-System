from datetime import datetime

class Transaction:
    """Represents a single transaction with details of amount, type, and timestamp."""
    def __init__(self, amount, transaction_type, description=""):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
        self.description = description

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: ${self.amount} ({self.description})"
