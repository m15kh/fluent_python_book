def factorial(n):
    """return n!"""
    return 1 if n < 1 else n * factorial(n - 1)


a1 = list(map(factorial, range(6)))
print(a1)

b1 = [factorial(x) for x in range(6)]
print(b1)

a2 = list(map(factorial, filter(lambda x: x % 2 == 0 , range(6))))
print(a2)

b2 = [factorial(x) for x in range(6) if x % 2 ==0]

print(b2)