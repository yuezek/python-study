'''
计算数字范围中的所有偶数
输入：begin=4， end=15 (不包括)
输出：[4,6,8,10,12,14]
'''

# 偶数-能被2整除的数，是2的倍数


def getEvenNumbers(begin, end):
    result = []
    for i in range(begin, end):
        if i % 2 == 0:
            result.append(i)
    return result


begin = 4
end = 15
print(f"begin={begin}, end={end}, even numbers: ", getEvenNumbers(begin, end))

# lambda表达式 - 一句话代码
data = [item for item in range(begin, end) if item % 2 == 0]
print(f"begin={begin}, end={end}, even numbers: ", data)
