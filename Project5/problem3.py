class Operation:
    def __init__(self, num=0):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num


a, b = map(int, input("输入数字：").split())
num1 = Operation(a)
num2 = Operation(b)

print(f'{num1.num} + {num2.num} = {num1 + num2}')
print(f'{num1.num} - {num2.num} = {num1 - num2}')
print(f'{num1.num} * {num2.num} = {num1 * num2}')
print(f'{num1.num} / {num2.num} = {num1 / num2}')

