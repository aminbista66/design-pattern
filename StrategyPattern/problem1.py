"""
Problem 1: Payment Method Selector

Scenario:
You are building an e-commerce checkout system. Customers can pay via Credit Card, PayPal, or Bank Transfer. Each method has different validation and processing steps.

Goal:
Design a system where adding a new payment method doesn’t require modifying existing code.

Hint:
Encapsulate payment behavior in separate strategy classes implementing a common PaymentStrategy interface.
"""

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def process(self):
        ...
    
    @abstractmethod
    def validate(self):
        ...

class CreditCardStrategy(PaymentStrategy):
    name: str = "Credit Card"
    
    def process(self):
        self.validate()
        print(f"{self.name} Payment Processed")

    def validate(self):
        print("Validation Successful")

class PaypalStrategy(PaymentStrategy):
    name: str = "PayPal"

    def process(self):
        self.validate()
        print(f"{self.name} Payment Processed")

    def validate(self):
        print("Validation Successful")

class BankStrategy(PaymentStrategy):
    name: str = "Bank"

    def process(self):
        self.validate()
        print(f"{self.name} Payment Processed")

    def validate(self):
        print("Validation Successful")

class PaymentProcessor:
    strategy: PaymentStrategy

    def setStrategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def pay(self):
        self.strategy.process()
    
if __name__ == "__main__":
    strategy = PaypalStrategy()
    processor = PaymentProcessor()
    processor.setStrategy(strategy)
    processor.pay()