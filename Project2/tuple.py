t1 = (1, "hello", 2)
t2 = ()
t3 = tuple()

print(t1)
print(t2)
print(t3)

print('\n')
t4 = ((1,2,3), (1,2, 5))
print(t4[1][2])
i = 0
j = 0
while i < len(t4):
    while j < len(t4[0]):
        print(t4[i][j])
        j += 1
    i += 1
