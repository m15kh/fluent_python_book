fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

x = sorted(fruits, key=len)
print(x)

def reverse(word):
    return word[::-1]
print(reverse('hello'))
print(sorted(fruits, key=reverse))