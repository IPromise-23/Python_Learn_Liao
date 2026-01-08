#对函数fact(n)编写doctest(文档测试)并执行：
def fact(n):#阶乘函数
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a positive integer
    '''
    if n < 1:
        raise ValueError('n must be a positive integer')
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
