from structs.abstract import Collection


class Stack(Collection):
    
    def add(self, item):
        self._items.append(item)

    def get(self):
        last_item = self._items.pop()
        return last_item
        

