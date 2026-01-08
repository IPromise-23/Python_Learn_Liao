# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'.':None}
def str2float(s):
    def fn(x,y):
        if x is None:
            return y
        if y is None:
            return x
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    parts = s.split('.')
    int_str = parts[0]
    frac_str = parts[1]
    int_part = reduce(fn, map(char2num, s.split('.')[0])) # 获取第一个元素：'123'（整数部分）
    frac_part = reduce(fn, map(char2num, s.split('.')[1])) # 获取第二个元素：'456'（小数部分）
    return int_part + frac_part /  (10 ** len(frac_str))
#s = '123.456'
#parts = s.split('.') # 分割字符串，返回一个列表：['123', '456']
#int_part = parts[0] # 获取第一个元素：'123'（整数部分）
#frac_part = parts[1] # 获取第二个元素：'456'（小数部分）

    

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')