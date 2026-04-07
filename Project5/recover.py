class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age
    def __str__(self):
        return f'{self.name} : {self.age}'
    def __repr__(self):
        return f'{self.name!r} : {self.age!r}'



p1 = Person('zhangsan', 18)
p2 = Person('lisi', 20)
p3 = Person('wangwu', 15)

lst = [p1, p2, p3]

lst1 = sorted(lst, key=lambda x : x.age)
print(lst1)

for i in lst1:
    print(i)
    
