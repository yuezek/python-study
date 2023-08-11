'''
求数字N的阶乘
6 的阶乘：6*5*4*3*2*1
3 的阶乘：3*2*1
....
就是就连续N个整数的乘积
输入： 数字N
输出： 连续N个整数的乘积
'''

def factorial(number):
    result = 1
    while number>0:
        result*=number
        number-=1
    return result    

print("阶乘 3 = ",factorial(3))
print("阶乘 6 = ",factorial(6))
print("阶乘 100 = ",factorial(100))