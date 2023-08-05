''' 
第2期-求100以内 奇数/偶数/自然数 的和 (累加求和)
使用四种方法
1. for
2. while
3. recusive - 仅仅是培养思想
4. 数学方法
'''

def sum(N):
    total = 0
    for i in range(1,N+1):
        total +=i
    return total

N = int(input("求N个连续自然数的和："))
print(sum(N))