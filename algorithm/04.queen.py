'''
N 皇后问题

长笑对人生 兔年好幸福！
--------------------
笑对人生好 兔年幸福长！
--------------------
'''

n=int(input("输入N:"))
'''
python列表推导式

list=[[0 for i in range(3)] for j in range(4)] 二维数组3*4

m=lambda x,y:x*y;
print m(2,9);
'''
#初始化二维数组
matrix=[[0 for i in range(n)]  for j in range(n) ]
#print(matrix)

# 检查皇后的位置
def check(x, y):
    # - 检查同一列
    for i in range(n):
        if matrix[i][y]==1 :
            return False
    # \ 检查斜线
    for i in range(n):
        for j in range(n):
            if x-y == i-j  and  matrix[i][j] == 1:
                return False
    # / 检查斜线
    for i in range(n):
        for j in range(n):
            if x+y == i+j and matrix[i][j] == 1:
                return False
    return True        
# 
count=0
def dfs(num):
    #遍历完毕
    if num ==n:
        #统计结果
        global count
        count+=1
        #将结果打印出来
        print("=======第 %2d 种解======="%(count))
        for a in matrix:
            print(a)
        return 
    #遍历所有行 - 每次都遍历到最后一行（尝试找到结果）
    for i in range(n):
        #假设前面行是正确放置的
        if check(num,i):
            #假设尝试成功
            matrix[num][i]=1
            #尝试下一行
            dfs(num+1)
            #尝试失败就回溯
            matrix[num][i]=0

#从第一行开始深度遍历
dfs(0)
print("总共有%d种解"%count)

'''
四皇后的解法：
1,0,0,0   
0,0,1,0    
0,0,0,1
0,1,0,0

0,1,0,0
0,0,0,1
1,0,0,0
0,0,1,0
'''

