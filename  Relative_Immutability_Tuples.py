from os import system as s
s('clear')

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(f"t1 is t2: {t1 is t2}")
print(f"t1 == t2: {t1 == t2}")
print(f"id t1 and id t2: {id(t1), id(t2)}")
print(f"id t1[-1] and id t2[-1]: {id(t1[-1]), id(t2[-1])}")

t2[-1].append(100)
print(t2)
print(t1)
print(f" after id t1 and id t2: {id(t1), id(t2)}")
print(f" after id t1[-1] and id t2[-1]: {id(t1[-1]), id(t2[-1])}")

print(f"t1 is t2: {t1 is t2}")
print(f"t1 == t2: {t1 == t2}")
