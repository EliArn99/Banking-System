from abc import ABC, abstractmethod


class TransactionHandler(ABC):
    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass
