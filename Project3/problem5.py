Sum = 0
cnt = 0
while True:
    Sum += int(input('请输入成绩：'))
    cnt += 1
    flag = input('是否继续：')
    if flag == 'no':
        break
    elif flag == 'yes':
        pass
avge = Sum / cnt
print(f'平均值是{avge}')