from os import system as s
s('cls')


a = [10, 20]
b = [a, 30]
print("b is:",b)
a.append(b)
print("a is:",a)
print("b is:",b)
from copy import deepcopy
c = deepcopy(a)
print("c is:",c)