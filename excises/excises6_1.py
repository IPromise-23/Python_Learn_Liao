#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1=255
print(str(hex(n1)))

print("输入待转换的整数：")
n=int(input())
print("%d的十六进制为"%n,str(hex(n)))