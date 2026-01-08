#请将本地一个文本文件读为一个str并打印出来：
# fpath = '/Users/ipromise/Desktop/VscodeforLearning/lxfclass/test_for_13.txt'
fpath = "test_for_13.txt"
with open(fpath, 'r') as f:
    s = f.read()
    print(s)

# 运行代码观察结果

#绝对路径(无论python脚本在哪儿,都能直接定位文件)
#/Users/ipromise/Desktop/VscodeforLearning/lxfclass/test_for_13.txt
#或者用主目录缩写形式(~代替用户主目录)
#import os
#path = os.path.expanduser("~/Desktop/VscodeforLearning/lxfclass/test_for_13.txt")
#相对路径(python脚本和test_for_13.txt在同一个文件夹下,可以直接写文件名)
#test_for_13.txt