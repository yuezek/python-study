'''
对简单列表排序
简单列表：元素类型不是复合类型(列表、元组、字典)
形式1：[20,50,10,40,30]
形式2：['bb','ee','aa','dd','cc']

知识点:
1.怎样原地排序？怎样不改变原列表排序？
2.怎样指定是升序还是降序？
'''

lista=[20,50,10,40,30]

#lista.sort()
#lista.sort(reverse=True)
#print(f"lista is sorted:",lista)

listb=sorted(lista)
print(f"lista is sorted:",lista)
print(f"lista is sorted:",listb)

listc=sorted(lista,reverse=True)
print(f"lista is sorted:",listc)