def factorial(n):
    """return n!"""
    return 1 if n < 1 else n * factorial(n - 1)


print(factorial(42))



fact = factorial
print(fact)
print(fact(42))
print("----------------")
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))