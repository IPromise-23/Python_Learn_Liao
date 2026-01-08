#第一题：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools

def metric(fn):
    @functools.wraps(fn)#保留原函数的元信息,如__name__
    def wrapper(*args,**kw):
        start_time = time.time()#记录函数执行前的时间
        res = fn(*args,**kw)#执行原函数,并保存返回值
        end_time = time.time()#记录函数执行后的时间
        exec_time = (end_time - start_time)*1000#计算执行时间并转换为ms
        print('%s executed in %s ms' % (fn.__name__, exec_time))
        return res#返回原函数的返回值(透传结果)
    return wrapper

# 测试
@metric#相当于执行语句 fast=metric(fast)
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f!= 33:
    print('测试失败!')
elif s!= 7986:
    print('测试失败!')
else:
    print('测试成功!')



#第二题：请编写一个decorator
#思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
#     pass
# #又支持：
# @log('execute')
# def f():
#     pass


import functools
def log(text=None):#log函数的参数text设置默认值None
    # 分支1：处理无参装饰器@log的情况（此时text是被装饰的函数）双层函数
    if callable(text):#callable()是内置函数,判断一个对象是否是“可以调用的”
    #当用@log时,py会把被装饰的函数直接传给log,此时text接收的是这个函数    
        fn = text#赋值语句,把text代表的原函数赋值给变量fn
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('begin call')
            res = fn(*args, **kw)
            print('end call')
            return res
        return wrapper
    # 分支2：处理带参装饰器@log('execute')的情况（此时text是传入的参数）三层函数
    else:
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print(f'begin call: {text}')
                res = fn(*args, **kw)
                print(f'end call: {text}')
                return res
            return wrapper
        return decorator
@log
def f1():
    print("__正在执行无参数@log")

@log('execute')
def f2():
    print("正在执行含参数@log__")

#编写一个decorator,能在函数调用的前后打印出'begin call'和'end call'的日志
# def log(fnc):
#     def wrapper(*args,**kw):
#         print('begin call')
#         res=fnc(*args,**kw)
#         print('end call')
#         return res
#     return wrapper

# @log
# def bar():
#     print('in bar')

#调用函数:
#bar()