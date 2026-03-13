
num = int(input('请输入一个三位正整数：'))
a = []
for i in range(0, 3, 1):
    a.append(num % 10)
    num //= 10
for i in range(len(a) - 1, -1, -1):
    print(a[i])
