a = []
for i in range(0, 3, 1):
    tmp = input('请输入字符串：')
    a.append(tmp)

if a[2] <= a[1] <= a[0]:
    print(a[2], a[1], a[0])
elif a[2] <= a[1] <= a[0]:
    print(a[2], a[1], a[0])
elif a[1] <= a[0] <= a[2]:
    print(a[1], a[0], a[2])
elif a[1] <= a[2] <= a[0]:
    print(a[1], a[2], a[0])
elif a[0] <= a[1] <= a[2]:
    print(a[0], a[1], a[2])
else:
    print(a[0], a[2], a[1])
# a = sorted(a)
# print(a)