
'''
工具库
'''
#交换数组中 第i和j位置 元素
#a: 数字数组
#i: 第i个位置
#j: 第j个位置
def swap(a , i , j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# 通过冒泡的方法让数组中的元素有序
# a： 无序的数字数组
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                swap(a,j, j+1)

# 找到数组中最大的元素
# a： 无序的数字数组
def max(a):
    m = a[0]
    for e in a:
        if e > m:
            m = e
    return m         

# 找到数组中最小的元素
# a： 无序的数字数组
def min(a):
    m = a[0]
    for e in a:
        if e < m:
            m = e
    return m         

# 求数字数组的总和
# a： 无序的数字数组
# 输入: 
# 输出:
def sum(a):
    t = 0
    for e in a:
        t += e
    return t

# 两个数相加
def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b