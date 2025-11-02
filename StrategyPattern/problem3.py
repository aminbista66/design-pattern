"""
Problem 3: Sorting Algorithm Chooser

Scenario:
You need to sort data differently depending on the situation (e.g., QuickSort for large datasets, BubbleSort for small ones).
You want to change sorting strategies at runtime based on conditions.

Hint:
Create a SortStrategy interface with implementations like QuickSort, MergeSort, and BubbleSort.

"""


from abc import ABC, abstractmethod

class SortStrategy(ABC):

    @abstractmethod
    def performSort(self, dataset):
        ...
    

class QuickSort(SortStrategy):
    name: str = "Quick Sort"
    
    def performSort(self, dataset):
        print(f"perfomed {self.name}")

class BubbleSort(SortStrategy):
    name: str = "Bubble Sort"
    
    def performSort(self, dataset):
        print(f"perfomed {self.name}")


class Sorter:
    strategy: SortStrategy

    def setStrategy(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def sort(self, dataset):
        if not self.strategy:
            raise ValueError("SortStrategy not set.")
        
        self.strategy.performSort(dataset)

class AlgorithmStrategyChooser:
    datasetSize: str

    def __init__(self, datasetSize="small"):
        self.datasetSize = datasetSize

    
    def getStrategy(self):
        if self.datasetSize == "small":
            return BubbleSort
        elif self.datasetSize == "large":
            return QuickSort
        else:
            raise ValueError("Unknown dataset size.")            

if __name__ == "__main__":
    chooser = AlgorithmStrategyChooser("large")
    strategyClass = chooser.getStrategy()
    sorter = Sorter()
    sorter.setStrategy(strategyClass())
    sorter.sort([1, 2, 3])

