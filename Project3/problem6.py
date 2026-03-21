def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


import datetime
today_date = datetime.date.today()
today_year = today_date.year
today_month = today_date.month
today_day = today_date.day
print(f'{today_year}年{today_month}月{today_day}')
#             1   2   3   4   5   6   7   8   9   10  11  12
list_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_day = 0
for i in range(0, today_month - 1):
    sum_day += list_month[i]

if is_leap_year(today_year) and today_month > 2:
    sum_day += 1

sum_day += today_day

print(f'今天是今年的第{sum_day}天')
