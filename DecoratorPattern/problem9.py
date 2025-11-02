"""
Problem 9: File Compression and Encryption

Scenario:
You are designing a system that processes data before saving to disk.
Data might need to be compressed, encrypted, or both — depending on user preference.

Goal:
Let users apply any combination of operations to data dynamically.

Hint:
Start with a DataSource interface and decorators like CompressionDecorator and EncryptionDecorator that wrap it.


"""

from abc import ABC, abstractmethod

class DataSourceInterface(ABC):
    @abstractmethod
    def operation(self):
        ...

class DataSource(DataSourceInterface):
    def operation(self):
        print("Raw data")

class Decorator(DataSourceInterface):
    _dataSource: DataSourceInterface

    def __init__(self, dataSource: DataSourceInterface) -> None:
        self._dataSource = dataSource

    def operation(self):
        self._dataSource.operation()

class CompressionDecorator(Decorator):
    def operation(self):
        self._dataSource.operation()
        print("Compressed Data")
    
class EncryptionDecorator(Decorator):
    def operation(self):
        self._dataSource.operation()
        print("Encrypted Data")

if __name__ == "__main__":
    dataSource = DataSource()
    dataSource = CompressionDecorator(dataSource)
    dataSource = EncryptionDecorator(dataSource)
    dataSource.operation()