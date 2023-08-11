'''
区间内的所有素数（质数）
输入：开始数字、结束数字
输出：开始到结束区间的所有素数
'''
import math
# 素数：如果数字只能被1和自己整除那它就是素数。
# 如1，2，3，5 都是素数
# 4 就不是素数
# 质数(prime number)是大于1的整数，并且只有两个正除数，1和它自己。前十个质数有：2,3,5,7,11,13,17,19,23和29。


def isPrimeNumber(number):
    if number in (1, 2):
        return True
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def printPrimeNumbers(begin, end):
    for num in range(begin, end+1):
        if isPrimeNumber(num):
            print(f"{num} is prime number")


begin = 11
end = 25

printPrimeNumbers(begin, end)
