from os import system as s
s("cls")
nasir_student = ['ali', 'reza', 'mahdi', 'mamad', 'bardia']   

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers  #BUG its buggy method! use must use self.passengers = list(passengers)
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

bus1 = Bus(nasir_student)
bus1.pick('malek')
bus1.drop('reza')
print(bus1.passengers)
print(nasir_student)
