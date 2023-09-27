import random
from os import system as s
s("cls")
class BingoCage:
    def __init__(self, items) -> None:
        self._items = list(items) 
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(30))
print(bingo())


class SayHello():
    def __init__(self, name):
        self.name = name
    def __call__(self):
        return f"Hello {self.name}"

x = SayHello("John")
print(x())