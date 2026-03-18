L = [10, 11, 12, 13, 14, 15]

for i in range(0, len(L), 1):
    if L[i] % 2 == 0:
        L[i] = L[i]**2
    else:
        L[i] = L[i]**3

print(L)