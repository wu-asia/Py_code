from math import cos
from math import pi
a = float(input('输入边长：'))
b = float(input('输入边长：'))
deg = float(input('输入角度（角度制）：'))
tmp = deg * (pi/180)
# cos(theta) = (a^2 + b^2 - c^2) / 2ab
c = ((a**2 + b**2) - cos(tmp)*2*a*b)**0.5
print(f'第三边是：{c}')
