'''
统计目录下的文件的大小：
1. 遍历目录
2. 文件的大小
3. 统计所有文件的size的和
'''

import os
print(os.path.getsize("basic\practice-100\Beginners-Guide.txt"))
#print(os.path.abspath("."))
#for f in os.listdir(os.path.abspath(".")+"\\basic\\practice-100"):
#    print(f)

#注意这个时候的当前目录是basci目录
basePath=os.path.abspath(".")+"\\basic"
for file in os.listdir(basePath+"\\practice-100"):
    print(f"{os.path.abspath(file)} > {os.path.isfile(os.path.abspath(file))}" )
    if(os.path.isfile(file)):
        print(f"{file} size :",os.path.getsize(os.path.abspath(file)))


for f in os.listdir("."):
    if(os.path.isfile(f)):
        print(f"{f} is file size :{os.path.getsize(f)}")
    else:
        print(f"{f} is dir")
        for f2 in os.listdir(f):
            print(f"\t{f2} : ",os.path.abspath(f2))
            if(os.path.isfile(f2)):
                print(f"\t\t{f2} is file size :{os.path.getsize(f2)}")
            else:
                print(f"\t\t{f2} is dir")   
