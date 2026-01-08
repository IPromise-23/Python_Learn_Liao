# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
# 请利用filter()筛选出回数：
from functools import reduce
def is_palindrome(n):
    digit_list=[int(d) for d in str(n)]#把整数数字转为字符串后，再把每个字符转为整数，放入列表
    digit_list_=digit_list[::-1]
    def mul(x,y):
        return x*10+y
    nn=reduce(mul,digit_list_)
    if n==nn:
        return n


# def is_palindrome(n):
#     s = str(n)
#     if s==s[::-1]:
#         return True
#     else:
#         return False
#s == s[::-1] 本身就是一个布尔值，要么是True，要么是False,所以没有必要再用if-else判断
#这题还有更简单的方法
# def is_palindrome(n):
#     s = str(n)
#     return s == s[::-1]
#把数字转为字符串后比较 s == s[::-1] 是判断回文最简单、直观且高效的方式


#digit_list.reverse() 会直接修改原列表 digit_list（比如把 [1,2,3] 改成 [3,2,1]），但它的返回值是 None（没有任何返回内容）。
#所以digit_list_=digit_list.reverse() 实际值是None

    # m=[]
    # for i in n:
    #     digit_list=[int(d) for d in str(i)]
    #     def mul(x,y):
    #         return x*10+y
    #     i_=reduce(mul,digit_list)
    #     if i==i_:
    #         m.append(i_)
    # return n and m   错误点：参数n应为整数，因为filter()和map()类似，已有一一对应关系，可以自己传入，无须for循环

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
#filter()函数返回的是一个Iterator，也就是一个惰性序列，
#所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
