def factorial(n):
    """return n!"""
    return 1 if n < 1 else n * factorial(n - 1)


print(factorial(42))

doc = factorial.__doc__
print(doc)

print(type(factorial))
