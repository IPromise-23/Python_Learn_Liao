# 假设我们有一组tuple表示学生名字和成绩
# 请用sorted()对下述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

#- t[0].lower - 这是 方法对象本身 （函数对象）,没有调用
#- t[0].lower() - 这是 调用方法 （执行函数并返回结果）


# L2 = sorted(L, key=by_name)
# print(L2)
# # 方法对象（没有调用）
# name = 'Bob'
# print(name.lower)    # <built-in method lower of str object>
# print(type(name.lower))  # <class 'builtin_function_or_method'>
# # 调用方法（执行函数）
# print(name.lower())  # 'bob'
# print(type(name.lower()))  # <class 'str'>


# 再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)