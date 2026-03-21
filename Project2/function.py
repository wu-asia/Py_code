
def func():
    return 1, 2, 3


x, y, z = func()
print(x, y, z, sep=' ',end='\n')

def add(x, y, z):
    return (x - y)*z


print(add(x = 1, y = 2, z = 4))

print(add(y = 2, x = 1, z = 4))

print(add(1, y = 2, z = 4))
print(add(y = 2, 1, z = 4))
