'''
读取成绩文件排序数据
输入文件：
    三列：学号，姓名，分数
    列之间用逗号分隔，比如 "001,张三,99"
    行之间用\n换行分割
处理：
    读取文件，按成绩倒序排列
输出：
    排序后的三列数据    
'''
def readFile(filePath, demiliter):
    result=[]
    #注意问题
    #1.路径为完整路径 - FileNotFoundError: [Errno 2] No such file or directory: './students.txt'
    #2.编码问题 -  UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 20: character maps to <undefined>
    with open(filePath, "+r",encoding="utf8") as fin:
        for line in fin:
            #去掉最后的换行符 - 注意如果最后没有空行的化 -这里隐藏一个bug
            line = line[:-1]
            #获取所有信息-用逗号分隔
            result.append(line.split(demiliter))
    return result

def sortGrade(datas):
    #分数在第三列,列表从0开始计数,
    #分数应该是整数-需要转换 - 注意不转换的bug - 万强居然跑
    #倒序排列
    return sorted(datas,
                    key=lambda x:int(x[2]), 
                    reverse=True)

#将数据用demiliter分隔的方式写到filePath文件中
def writeFile(datas, demiliter, filePath):
    with open(filePath,"w", encoding="utf-8") as fout:
        for data in datas:
            fout.write(demiliter.join(data)+"\n")

#1. 读取文件
# FileNotFoundError: [Errno 2] No such file or directory: "'./students.txt'"
datas=readFile("C:/Users/Kingmax_Kong/projects/github/python-study/basic/practice-100/students.txt",",")    
print(f"read file:",datas)
#2. 排序数据
datas=sortGrade(datas)
print(f"sort grade:",datas)
#3. 输出数据、写入文件
writeFile(datas,",","C:/Users/Kingmax_Kong/projects/github/python-study/basic/practice-100/students-sorted.txt")