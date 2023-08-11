'''
列表中所有数字的和
输入：列表                  [17,5,3,5]
输出：列表中所有数字的和      30
'''

def sumOfList(listParameter):
    total=0
    for i in listParameter:
        total+=i
    return total

list1 = [1,2,3,4]
list2 = [17,5,3,5]

print(f"sum of {list1}: ",sumOfList(list1))
print(f"sum of {list2}: ",sumOfList(list2))