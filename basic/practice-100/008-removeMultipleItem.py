'''
从列表中移除多个元素
输入：
    原始列表：  [3,5,7,9,11,13]
    移除列表:   [7,11]
输出：
    [3,5,9,13]
'''


def removeElementFromList(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista


lista = [3, 5, 7, 9, 11, 13]
listb = [7, 11]
print(f"from {lista} remove {listb} ,result: ",
      removeElementFromList(lista, listb))

# 一句代码实现 - lamda表达式
lista = [3, 5, 7, 9, 11, 13]
listb = [7, 11]
data = [item for item in lista if item not in listb]
print(f"from {lista} remove {listb} ,result: ", data)

