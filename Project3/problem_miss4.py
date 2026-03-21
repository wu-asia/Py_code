Sum = 0
for i in range(1, 21):
    ret = 1
    for j in range(1, i + 1):
        ret *= j
    Sum += ret

print(Sum)