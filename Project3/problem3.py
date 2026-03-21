num = int(input('请输入一个数字：'))
if num == 1:
    print(f'{num}不是素数')
else:
    flag = 1
    i = 2
    while i <= num:
        if num % i == 0:
            flag = 0
            break
        i += 1

    if(flag):
        print(f'{num} 是素数')
    else:
        print(f'{num} 不是素数')
