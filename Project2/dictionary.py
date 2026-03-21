d1 = {'key1':111, 'key2':23, 'key3':1}
print(max(d1))
print(max(d1.values()))

for i in d1.values():
    print(i)


t1 = (1, 23, 4)
print(max(t1))

l1 = list(d1)
print(l1)
l2 = list(d1.values())
print(l2)
l3 = list(t1)
print(l3)
s1 = set(d1)
s2 = set(d1.values())
print(s1, s2)