class Queue():
    
    def __init__(self):
        self._items = []
    
    def __bool__(self):
        return len(self._items) > 0

    def add(self, item):
        self._items.append(item)

    def get(self):
        first_item = self._items.pop(0)
        return first_item