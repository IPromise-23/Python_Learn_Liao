# Python提供的sum()函数可以接受一个list并求和
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

from functools import reduce

def prod(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)
#reduce()把一个函数mul作用在一个序列L上,
#这个函数mul必须接收两个参数，reduce把结果继续和序列的下一个元素作累积计算
#因此如果要调用reduce()，必须先构造一个能够接收两个参数的函数，放置在reduce()的第一个参数上

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')