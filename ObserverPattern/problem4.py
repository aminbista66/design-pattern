"""
Problem 4: Stock Market Notifier

Scenario:
You are creating a stock monitoring app. Whenever a stock’s price changes, all subscribed users (observers) must be notified.

Goal:
Implement a publisher-subscriber system where new types of observers (mobile app, web dashboard, etc.) can easily be added.

Hint:
Make Stock the Subject, and investors or dashboards the Observers.

"""

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, price: float):
        ...

class Subject(ABC):

    @abstractmethod
    def addObserver(self, observer: Observer):
        ...
    
    @abstractmethod
    def removeObserver(self, observer: Observer):
        ...

    @abstractmethod
    def notifyObservers(self):
        ...

class Stock(Subject):
    price: float

    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self.price = 0
    
    def addObserver(self, observer: Observer):
        self._observers.append(observer)
    
    def removeObserver(self, observer: Observer):
        self._observers.remove(observer)
    
    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self.price)
    
    # helper function
    def updateStockPrice(self, price):
        self.price = price
        self.notifyObservers()

class MobileApp(Observer):
    def update(self, price: float):
        print(f"[Mobile App] Stock Price Updated: ${price}")

class WebDashboard(Observer):
    def update(self, price: float):
        print(f"[Web Dashboard] Stock Price updated: ${price}")

if __name__ == "__main__":
    stock = Stock()
    mobileApp = MobileApp()
    webDashboard = WebDashboard()
    stock.addObserver(mobileApp)
    stock.addObserver(webDashboard)
    stock.updateStockPrice(230)
    stock.updateStockPrice(130)
    stock.updateStockPrice(30)
    