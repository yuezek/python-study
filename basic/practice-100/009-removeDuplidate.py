'''
怎样对python列表元素去重
输入：[10,20,30,10,20]
输出：[10,20,30]
'''
def getUniqueList(lista):
    result=[]
    for item in lista:
        if item not in result:
            result.append(item)
    return result        

lista = [10,20,30,10,20]
#listb = [10,20,30]
print(f"source {lista} unique list:", getUniqueList(lista))
#利用set不能重复的特性
print(f"source {lista} unique list:", list(set(lista)))
#利用字典的key不能重复的特性
print(f"source {lista} unique list:", {}.fromkeys(lista).keys())

#利用lambda来简化写法-类似hashmap的写法-缓存（不存在就放入）
temp=[]
[temp.append(item) for item in lista if not item in temp]
print(f"source {lista} unique list:", temp)

print(f"source {lista} unique list:", sorted(set(lista), key=lista.index))

# 删除列表中的重复项
data=[item for item in lista if lista.count(item)==1]
print(f"source {lista} unique list:",  data)
data=list(filter(lambda x: lista.count(x)==1,lista))
print(f"source {lista} unique list:",  data)

