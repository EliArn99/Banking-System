from abc import ABC, abstractmethod


class BalanceManager(ABC):
    @abstractmethod
    def get_balance(self) -> float:
        pass
