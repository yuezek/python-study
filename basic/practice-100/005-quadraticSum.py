'''
前N个数字的平方和
输入：数字N
输出：连续N个整数的平方的和
'''

def sumOfSquare(n):
    result = 0
    for i in range(1, n+1):
        result += i*i
    return result

print("sum of square 3 : ", sumOfSquare(3))
print("sum of square 5 : ", sumOfSquare(5))
print("sum of square 10 : ", sumOfSquare(10))
