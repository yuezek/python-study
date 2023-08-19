'''
统计一篇文章中单词出现的次数
这里统计top10
'''
article = "C:/Users/Kingmax_Kong/projects/github/python-study/basic/practice-100/Beginners-Guide.txt"
# 字典统计表
wordsCount = {}

with open(article, mode="r", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            # 不存在就放入统计字典
            if word not in wordsCount:
                wordsCount[word] = 0
            # 存在就将单词数增加1
            wordsCount[word] += 1
# 打印top10
# 1. 排序
# 2. 切片
print(sorted(wordsCount.items(),
             key=lambda x: x[1],
             reverse=True
             )[:10]
      )
