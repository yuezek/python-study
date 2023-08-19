'''
统计成绩
输入文件：
    三列：学号，姓名，分数
    列之间用逗号分隔，比如 "001,张三,99"
    行之间用\n换行分割
输出：
    最高分、最低分、平均分   
'''

def computeScore(filePath):
    # 将文件中的分数读取到列表中
    scores = []
    with open(filePath, mode="r", encoding="utf-8") as fin:
        for line in fin:
            # 去掉换行符
            line = line[:-1]
            # 用逗号分隔
            fields = line.split(",")
            # 获取分数列（也是最后一列）并转化为整数
            scores.append(int(fields[-1]))
    # 利用自带函数计算多个值
    maxScore = max(scores)
    minScore = min(scores)
    avgScore = round(sum(scores)/len(scores), 2)
    # 返回多个值
    return maxScore, minScore, avgScore


maxScore, minScore, avgScore = computeScore(
    "C:/Users/Kingmax_Kong/projects/github/python-study/basic/practice-100/students.txt")
print(f"maxScore = {maxScore}, minScore={minScore}, avgScore={avgScore}")
