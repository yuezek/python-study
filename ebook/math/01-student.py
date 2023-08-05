'''
----------------------------
书生分卷：
----------------------------
毛诗春秋周易书，九十四册共无余。
毛诗一册三人读，春秋一本四人呼。
周易五人读一本，要分每样几多书。
就见学生多少数，请君布算莫踌躇。
----------------------------
'''

a = []
x = 1
'''
while x < 94:
    student = x * 3
    c = student // 4
    z = student // 5
    if x + c + z == 94:
        #a.append("学生数："+str(student))
        #a.append('《毛诗》：'+str(x))
        #a.append('《春秋》：'+str(c))
        #a.append('《周易》：'+str(z))
        a.append("学生数：%s"%(student))
        a.append('《毛诗》%s'%(x))
        a.append('《春秋》%s'%(c))
        a.append('《周易》%s'%(z))
    x += 1
'''

for x in range(94):
    student = x * 3
    c = student // 4
    z = student // 5
    if x + c + z == 94:
        a.append("学生数：%s"%(student))
        a.append('《毛诗》%s'%(x))
        a.append('《春秋》%s'%(c))
        a.append('《周易》%s'%(z))
    #x +=1 
    
print(a)

    