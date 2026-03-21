num = int(input('输入菱形的底座长度：'))

for i in range(0, num // 2):
    for j in range(0, num):
        if (num//2 - 1 - i) <= j <= (num//2 + i):
            print('*',end='')
        else:
            print(' ',end='')
    print(end = '\n')

for i in range(num // 2 - 1, -1, -1):
    for j in range(0, num):
        if (num // 2 - 1 - i) <= j <= (num // 2 + i):
            print('*', end='')
        else:
            print(' ', end='')
    print(end='\n')

