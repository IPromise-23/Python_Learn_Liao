#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

#someone@gmail.com
#bill.gates@microsoft.com

import re

def is_valid_email(addr):
    # 定义正确的邮箱验证正则表达式
    # ^          匹配字符串开头
    # [a-zA-Z0-9.]+  匹配用户名：字母、数字、点（.），至少1个字符
    # @          匹配@符号（无需转义，在正则中@不是特殊字符）
    # [a-zA-Z0-9]+   匹配域名主体（如gmail、microsoft）：字母、数字，至少1个字符
    # \.com$     匹配.com结尾（\.转义点，$匹配字符串结尾）
    pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.com$'
    # re.match返回匹配对象（成功）或None（失败），用bool()转成True/False返回
    return bool(re.match(pattern, addr))

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

#版本二可以提取出带名字的Email地址：

#<Tom Paris> tom@voyager.org => Tom Paris
#bob@example.com => bob

import re

def name_of_email(addr):
    # ^          匹配字符串开头
    # (?:<([\w\s]+)>\s)?  非捕获组（?:），表示这部分“可选”（?）；
    #                     其中<([\w\s]+)> 捕获尖括号内的名字（\w匹配字母和数字，\s匹配空格）
    # ([\w]+)@   捕获@前面的用户名（普通Email的名字）
    pattern = r'^(?:<([\w\s]+)>\s)?([\w]+)@'#正则表达式已经定义了分组,明确用()定义了捕获分组
    #正则里()才是“分组”,只有用()包裹的部分才是正则的捕获分组,group()方法就是对应这些()包裹的分组的
    #这里有2个捕获分组,第一个捕获分组：([\w\s]+)_用来匹配尖括号里的名字,第二个捕获分组：([\w]+)_用来匹配@前面的用户名
    #(?:<...>)是非捕获组（?:表示 “这个组不参与捕获，不算入分组序号”），但它内部的([\w\s]+)依然是 “捕获分组”，会被算入group()的序号。
    match_result = re.match(pattern,addr)
    
    if match_result:
        # 取出两个分组：group1是尖括号里的名字，group2是@前的用户名
        name_in_angle, username = match_result.groups()#返回所有捕获分组的结果组成的元组
        # 有尖括号的名字就返回它，否则返回用户名
        return name_in_angle if name_in_angle else username
    return None  # 匹配失败时返回None（测试用例都是合法的，可忽略）

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
