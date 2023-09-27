fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

s = sorted(fruits, key= lambda word : word[::-1])
print(s)