# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name.title()#title()函数可以将字符串中每个单词的首字母大写，其余字母小写

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
#`map()`函数将传入的函数依次作用到可迭代对象的序列的每个元素，并把结果作为新的可迭代对象返回。
print(L2)
#通过map(normalize, L1)可以将L1列表中的每个元素依次传入normalize函数进行处理，
#再用list()将处理结果转换为列表，最终得到规范后的名字列表。