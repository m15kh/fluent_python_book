from os import system as s
s("cls")

class HauntedBus:
    """A bus model haunted by ghost passengers"""
    def __init__(self, passengers=[]): #BUG its buggy method! use None for passengers and condotion method
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

print('-----------------------')
print(HauntedBus.__init__.__defaults__)
print('-----------------------')

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)

print(bus1.passengers)
print("-----------------------")
print(HauntedBus.__init__.__defaults__)
print('-----------------------')
