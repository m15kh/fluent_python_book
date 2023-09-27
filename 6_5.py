from os import system as s
s('cls')

t1 = (1, 2, [30, 40])



print(f"id t1:{id(t1)}")
print()
print(f"id t1[-1]:{id(t1[-1])}")
print()
t1[-1].append(100)
print(t1)
print()
print("after change ")
print()
print(f"id t1:{id(t1)}")
print()
print(f"id t1[-1]:{id(t1[-1])}")
print()

print("-----------------------------")
lst1 = [1,34343,43]
print(f"id lst1{id(lst1)}")
lst1.append(100)
print(f"id lst1{id(lst1)}")


