#利用循环依次对list中的每个名字打印出Hello, xxx!
names = ['Alice', 'Bob', 'Charlie', 'David']
#用两种循环语句，for和while，分别实现上述功能。
for name in names:
    print('Hello,',name+'!')

i=0
while i < len(names):
    print('Hello,',names[i]+'!')
    i =i+ 1