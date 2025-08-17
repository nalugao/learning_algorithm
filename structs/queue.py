from structs.abstract import Collection


class Queue(Collection):
    
    def add(self, item):
        self._items.append(item)

    def get(self):
        self._items.pop(0)
