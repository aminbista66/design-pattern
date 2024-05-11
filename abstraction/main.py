from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        ...

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self) -> int:
        return 3.14 * self.radius ** 2
    
circle = Circle(10)

print(circle.area())