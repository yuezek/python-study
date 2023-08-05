import util as util
a=[1,2,3,4,5]
#for i in range(len(a)):
#    #i+=1
#    print(a[i])

#################
print(util.max(a))
a=[1,6,8,4,2]
print(util.max(a))
print(util.min(a))
print(util.sum(a))
##################

#连续n个自然数的和
def sum(n):
    if n < 1: 
        return n
    else:
        return sum(n-1)+n
#    
print(sum(5))  
# 
a=[1,2,3,4,5]
print(util.sum(a))
