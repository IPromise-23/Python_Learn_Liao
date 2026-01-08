#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    return float(s) 
    #return int(s)     #这是报错的源头

def calc(exp):#计算以+连接的数字字符串表达式的总和
    ss = exp.split('+')#exp是传入字符的表达式,split('+')把字符串按+分割成列表
    ns = map(str2num, ss)#map(函数,可迭代对象),会把str2num函数依次应用到ss的每个元素上
    #map()返回的ns是一个迭代器(特点:惰性计算、打印ns只能看到迭代器对象的内存地址、只能被遍历一次)
    #即如果用过了list(ns),说明迭代器ns已经被list()遍历过,现在是空的,需要重新生成
    #reduce是累加器,遍历ns(迭代器)中的元素,通过lambda函数将元素逐步累加
    #reduce(函数,序列),reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    return reduce(lambda acc, x: acc + x, ns)#这里ns是序列,匿名函数lambda acc, x: acc + x为函数

#对calc中的变量说明:
#例如测试calc('100 + 200 + 345')
#ss:['100 ', ' 200 ', ' 345']
#直接打印ns(迭代器):<map object at 0x7fc761bc3940>
#转换为列表list(ns):[100.0, 200.0, 345.0],并且注意转换为列表后ns已经被遍历,现在是空的,要重新生成,否则在reduce()中是不可用的

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()


#运行后结果如下:

#(base) ipromise@ipromisedeMac-mini lxfclass % /usr/local/bin/python3 /Users/ipromise/Desktop/VscodeforLearning/lxfclass/excises12_1.py
# 100 + 200 + 345 = 645
# Traceback (most recent call last):
#   File "/Users/ipromise/Desktop/VscodeforLearning/lxfclass/excises12_1.py", line 29, in <module>
#     main()
#     ~~~~^^
#   File "/Users/ipromise/Desktop/VscodeforLearning/lxfclass/excises12_1.py", line 26, in main
#     r = calc('99 + 88 + 7.6')
#   File "/Users/ipromise/Desktop/VscodeforLearning/lxfclass/excises12_1.py", line 15, in calc
#     return reduce(lambda acc, x: acc + x, ns)#这里ns是序列,匿名函数lambda acc, x: acc + x为函数
#   File "/Users/ipromise/Desktop/VscodeforLearning/lxfclass/excises12_1.py", line 6, in str2num
#     return int(s)
# ValueError: invalid literal for int() with base 10: ' 7.6'