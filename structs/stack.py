class Stack:

    def __init__(self):
        self._items = []
    
    def __bool__(self):
        return len(self._items) > 0
    
    def add(self, item):
        self._items.append(item)

    def get(self):
        last_item = self._items.pop()
        return last_item
        

