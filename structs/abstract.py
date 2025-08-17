from abc import ABC, abstractmethod


class Collection(ABC):

    def __init__(self):
        self._items = []

    @abstractmethod
    def add(self, item):
        """Add an item to the collection."""
        pass

    @abstractmethod
    def get(self):
        """Remove and return the item from the collection."""
        pass

    def __bool__(self):
        """Check if the collection is not empty."""
        return bool(self._items)
