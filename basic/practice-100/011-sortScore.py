'''
怎样实现学生成绩排序 - 复杂列表 （元素是字典或元组）
[
    {'no':101,'name':'小张','grade':88},
    {'no':102,'name':'小王','grade':77},
    {'no':103,'name':'小李','grade':99},
    {'no':104,'name':'小赵','grade':66},
    {'no':105,'name':'小孔','grade':100}
]
'''


students = [
    {'no': 101, 'name': '小张', 'grade': 88},
    {'no': 102, 'name': '小王', 'grade': 77},
    {'no': 103, 'name': '小李', 'grade': 99},
    {'no': 104, 'name': '小赵', 'grade': 66},
    {'no': 105, 'name': '小孔', 'grade': 100}
]
# 将学生表(students)按照分数(key)降序(reverse)排列(sorted)输出
# lambda 简单解释
# key 是一个表达式： 
#   入参 x 是列表中的每一个元素
#   返回值 是元素中的score的值
# reverse=True - 按降序排列
studentsSorted = sorted(students, key=lambda x: x["grade"], reverse=True)

print(f" source:\n {students} \n sort result:\n {studentsSorted}")

#print(students)
#print(studentsSorted)
