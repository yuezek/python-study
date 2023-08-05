'''
简易计算器 
- 理解函数的定义和使用
- 简单工程思路
- 不考虑溢出和数据类型检查（数字字符）

制作简易计算器实现两数加减乘除等运算，可以分为以下三个步骤：
1. 请用户输入待运算的两个数字
2. 请用户选择运算方法
3. 将运行结果展示出来
'''
import util as u

a = float(input("输入第一个数："))
b = float(input('输入第二个数：'))
c = input('输入一个运算符：')
if c == '+':
    print(u.add(a,b))
elif c == '-':
    print(u.subtract(a,b))
elif c == '*':
    print(u.multiply(a,b))
elif c == '/':
    print(u.divide(a , b))
else:
    print('运算符输入错误!')

