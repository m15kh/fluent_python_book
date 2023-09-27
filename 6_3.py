from os import system as s
s("cls")
l1 = (1,2,3,4,5)

print("tag object")
l2 = l1
print(f"l1:{id(l1)}\nl2:{id(l2)}")

print("shallow copy")
x1 = (1,2,3)
x2 = list(x1)
print(f"x1:{id(x1)}\nx2:{id(x2)}")

