
d1 = {"格力电器":7.0, "中石油":6.3, "深高速":4.2}

print(f'最高价是{max(d1.values())}')
print(f'最低价是{min(d1.values())}')
l1 = sorted(d1.values(), reverse=True)
print(l1)