class Goods:
    ids = None
    name = None
    price = None
    def __init__(self, ids = '', name = '', price = 0.0):
        self.ids = ids
        self.name = name
        self.price = price

lst = []
for i in range(0, 4):
    ids = input("输入产品编号:")
    name = input("输入产品名称:")
    price = float(input("输入产品价格:"))
    lst.append(Goods(ids, name, price))

ret = 0
for e in lst:
    ret += e.price
#ret = sum(map(lambda x : x.price, lst))
print(f"价格结果是{ret}")