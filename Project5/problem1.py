class Add:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def addition(self, x, y, z):
        return x + y + z


a, b, c = map(int, input("输入数字：").split())
op = Add(a, b, c)
print(op.addition(a, b, c))
