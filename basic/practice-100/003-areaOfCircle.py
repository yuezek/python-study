'''
求圆的面积
输入：圆的半径  
输出：圆的面积
'''
import math
# print(math.pi)
# 圆面积公式 - Π 和 平方计算
# round函数-保留两位小数

def areaOfCircle(r):
    return round(math.pi*r*r, 2)


print("Area of 2 is :", areaOfCircle(2))
print("Area of 3.1 is :", areaOfCircle(3.14))
print("Area of 6.78 is :", areaOfCircle(6.78))
