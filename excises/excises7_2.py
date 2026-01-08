#请使用迭代查找一个list中最小和最大值，并返回一个tuple
# def findMinAndMax(L):
#     if L==[]:
#         return(None,None)
#     else:
#         max=min=L[0]
#         i=0
#         while i < len(L):
#             if L[i]>=max:
#                 max=L[i]
#             else:
#                 max=max   #事实上11、12行以及下面的15、16行else语句都可以省略不写
#             if L[i]<=min:
#                 min=L[i]
#             else:
#                 min=min
#             i+=1
#         return (min, max)

# def findMinAndMax(L):
#     if L==[]:
#         return(None,None)
#     else:
#         min=max=L[0]
#         for i in L:
#             if i>max:
#                 max=i
#             if i<min:
#                 min=i
#         return(min,max)
    
def findMinAndMax(L):
    if L==[]:
        return(None,None)
    else:
        max=min=L[0]   #注意这一步要放在for循环外，否则每次都重置了最值，比较的结果无法积累
        for i in L:
            if not isinstance(i, (int, float)):
                raise TypeError('参数错误')    #优化行
            if i>=max:
                max=i
            if i<=min:
                min=i
        return(min,max)

        
# def findMinAndMax(L):
#     if L == []:  # 列表为空时
#         return (None, None)
#     else:  # 列表非空时
#         max = min = L[0]
#         i = 0
#         while i < len(L):
#             if L[i] >= max:
#                 max = L[i]
#             if L[i] <= min:
#                 min = L[i]
#             i += 1
#         return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')