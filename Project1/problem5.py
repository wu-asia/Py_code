a = [1, 2, 3, 4]
b = (5, 6, 7, 8)

a, b = list(b), tuple(a)

print(a)
print(b)