"""
Problem 8: Text Editor with Formatting

Scenario:
You are creating a text editor that allows applying styles like bold, italic, or underline to text.
Users can combine multiple styles.

Goal:
Allow adding or removing styles dynamically without altering the base text class.

Hint:
Use a Text component and decorators like BoldDecorator, ItalicDecorator, etc., that modify the display or rendering.

"""
from abc import ABC, abstractmethod

class TextInterface(ABC):
    @abstractmethod
    def style(self):
        ...


class Text(TextInterface):
    def style(self):
        print("normal style")

class Decorator(TextInterface):
    _text: TextInterface

    def __init__(self, text: TextInterface) -> None:
        self._text = text
    
    def style(self):
        self._text.style()
    

class BoldDecorator(Decorator):
    def style(self):
        self._text.style()
        print("Bold style")

class ItalicDecorator(Decorator):
    def style(self):
        self._text.style()
        print("Italic style")


if __name__ == "__main__":
    text = Text()
    text = BoldDecorator(text)
    text = ItalicDecorator(text)

    text.style()