#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    m=0
    n=1
    while m<len(s):#为了防止越界,所以要小于len(s)
        if s[m]!=' ':
            break
        m+=1
    while n<=len(s):
        if s[-n]!=' ':
            break
        n+=1
    return  s[m:len(s)-n+1]

#下面给出标准答案
def trim(s):
    start = 0
    end = len(s)
    # 跳过开头空格
    while start < end and s[start] == ' ':
        start += 1
    # 跳过结尾空格（end 指向切片结束位置，不包含）
    while end > start and s[end - 1] == ' ':
        end -= 1
    return s[start:end]
# s[-1:0]返只会回空字符串，不会检查最后一个字符，导致n始终为0，函数不会去掉末尾空格。   s[-1:]才会返回最后一个字符
#负索引切片在按位检查场景容易出错。更健壮的方法是用两个指针 start/end，start从前向后移动，end从后向前移动（end 指向切片的结束位置）。
    
# print(trim('  hello'))
# print(trim('hello  '))
# print(trim('  hello'))
# print(trim('  hello  '))
# print(trim('  hello  world  '))
# print(trim('    '))
# print(trim(''))

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


#补充，统计字符串中非空格字符的个数
def count_non_space(s):
    count = 0
    for char in s:
        if char == ' ':
            continue  # continue跳过现在的循环,执行下一次循环,,跳过空格，不计数
        count += 1  # 非空格才计数
    return count

print(count_non_space('  hello world  '))  # 输出10（h-e-l-l-o-w-o-r-l-d）