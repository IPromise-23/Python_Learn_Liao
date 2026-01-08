#以下函数允许计算两个数的乘积，请给函数添加必要的代码以实现计算一个或者多个数的乘积
def mul(x, *args):
    result = x
    for n in args:
        result = result * n
    return result

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:   #！=表示不等运算
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')


#我觉得可以用def mul(x,*args)： result=x
# for n in args:    result=result*n   return result
