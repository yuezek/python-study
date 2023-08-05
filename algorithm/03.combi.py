'''
巴斯卡三角形、杨辉三角
'''

#define N 12
#计算出第N层第r个数字
#def combi(n, r):
#    p = 1
#    for i in range(1, r+1):
#        p = p *(n-i+1) // i
#    return p
#
#def paint(N):
#    #总共多少层
#    for n in range(N+1):
#        #处理第N层的n个数字 
#        # 第N层有N个数字
#        for r in range(n):
#            #排版设定开始 
#            if(r == 0):
#                #第一层将空格控出来
#                for i in range(N-n+1):
#                    print("  ", end=" ")
#            else:
#                print("  ", end=" ")
#            #/* 排版设定结束 */
#            print("%3d"%combi(n, r), end=" ")
#        print("")
#
#N = int(input("请输入层数:"))
#paint(N)

'''
杨辉三角的性质：

每行首尾的数字都是1
每行中间的各数都是它肩上两个数的和
第n行的数字有n项
第n行的项数总比n-1行多1个
'''
n = int(input("输入需要打印的杨辉三角行数 :"))
assert n > 0, "请输入正整数！"

resultTable = []
for i in range(n):
    list2 = []
    if i == 0:
        list2 = [1]
    elif i == 1:
        list2 = [1, 1]
    else:
        for j in range(i + 1):
            if j == 0 or j == i:
                list2.append(1)
            else:
                list2.append(resultTable[i - 1][j - 1] + resultTable[i - 1][j])
    resultTable.append(list2)

space = len(resultTable[-1])
for i in resultTable:
    print(' ' * (space * 4 // 2), end='')
    for j in i:
        print(f"{j:<4}", end='')
    print()
    space -= 1