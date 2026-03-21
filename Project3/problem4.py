big = 3
mid = 2
small = 0.5
total = 100 #有多少担
num = 100 #有多少马
maxi = total // big
maxj = total // mid
cnt = 0
for i in range(0, maxi + 1):
    for j in range(0, maxj + 1):
        if (total - big*i - mid*j)  / small == num - i - j:
            print(f'大马:{i}, 中马:{j}, 小马:{num - i - j}')
            cnt += 1

print(f'总共有{cnt}种方案')