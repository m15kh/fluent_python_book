from os import system as s
s("cls")

def f(a,b):
    a += b
    return a

x1 = 2
y1 = 3
print(f(x1,y1))
print("x1 is {0} and y1 is {1}".format(x1,y1))

x2 = [1,2]
y2 = [3,4]
print(f(x2,y2))
print("x2 is {0} and y2 is {1}".format(x2,y2))


x3 = (1,2)
y3 = (3,4)
print(f(x3,y3))
print("x3 is {0} and y3 is {1}".format(x3,y3))