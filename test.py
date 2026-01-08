#  print('''1
#  2
#  3''')

#  print(r'''hello,\n
#  world''')

#  age=input("请输入你的年龄：")
#  if int(age)>=18:
#  input() 返回的是字符串（str）。if 里要和数字比较（如 18），必须先把字符串转换为数值类型，
#  否则会抛出 TypeError（在 Python 3 中 str 和 int 不能直接比较）
#  int(age) 就是把用户输入从字符串变成整数，才能做数值比较。
#      print("你已经成年了")
#  else:
#      print("你还未成年")

#  a=123
#  print(a)
#  a="ABC"
#  print(a)

# a="abc"
# b=a
# a=123
# print(a,b)

# x1=ord('A')  # 65
# x2=chr(65)  # 'A'
# print(x1,x2)

# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

# classmates=['Michael','Bob','Tracy']
# classmates.append('Adam')  # 添加元素到末尾
# classmates.insert(1,'Jack')  # 插入元素到指定位置
# classmates.pop()  # 删除末尾元素
# classmates.pop(1)  # 删除指定位置元素
# classmates[0]='Michael'  # 替换指定位置元素
# classmates[0]  # 'Michael'
# classmates[1]  # 'Bob'
# classmates[2]  # 'Tracy'

# if 1:
#     print('True')

# age = 17
# match age:
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')

# args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']
# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')

# n = 0
# while n < 10:
#     if n%2==1:
#         continue
#     n = n + 1
#     print(n)

# names=['Michael','Bob','Tracy']
# scores=[95,75,85]
# i=0
# for i in range(len(names)): 
#     if names[i]=='Bob':
#         print(scores[i])
#         break
#     i=i+1

# d={'Michael':95,'Bob':75,'Tracy':85}
# # print('A' in d)
# print(d.get('Bob',-1))

# print(len(str('')))    #0个字符，一个''
# print(len(str(' ')))   #1个字符，注意和上一个区分，这个是' ',是有空格的
# print(len(str('a ')))  #2个字符，一个'a'一个' '
# l=[1,2,3,4,5,6]
# print(l[-1:])
# print(l[-2:])
# print(l[-2:-1])

# L=[1,2,3,4,5,6]
# n=0
# for i in L:
#     L[n]=i*i
#     n+=1
# print(L)

# import os # 导入os模块，模块的概念后面讲到
# [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

# L=(x for x in range(10))
# next(L)

# # 首先获得Iterator对象:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break

# def char2num(s):
#      digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#      return digits[s]
# char2num('13579')

# t=('Bob', 75)
# print(t[0])

# print(range(1,100))

# kw = { 'base': 2 }
# print(int('1000000', **kw))

# d={'Michael':95,'Bob':75,'Tracy':85}
# print(d.get('a',-1))
# print(d.get('Michael'))

# import time, functools
# # def fast(x, y):
# #     time.sleep(0.0012)
# #     return x + y
# # print(fast(11,22))
# def metric(fn):
#     def wrapper(*args, **kw):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args, **kw)
#     return wrapper
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
# fast(11,22)

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# class Animal(object):   #编写Animal类
#     def run(self):
#         print("Animal is running...")

# class Dog(Animal):  #Dog类继承Amimal类，没有run方法
#     pass

# class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
#     def run(self):
#         print('Cat is running...')
#     pass

# class Car(object):  #Car类不继承，有自己的run方法
#     def run(self):
#         print('Car is running...')

# class Stone(object):  #Stone类不继承，也没有run方法
#     pass

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
# run_twice(Car())
# run_twice(Stone())

# print(1024*768)

# n=[5,6,4,7,8,3]
# start = n.start
# stop = n.stop
# print('start:'% "," 'stop:'% %(start,stop))

# args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']
# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('Hello，%s'%x)

#利用循环依次对list中的每个名字打印出Hello, xxx!
# names = ['Alice', 'Bob', 'Charlie', 'David']
# #用两种循环语句，for和while，分别实现上述功能
# for name in names:
#     print('Hello,',name+'!')
#     print('Hello,%s!'%name)   #另一种形式
# #while语句
# i=0
# while i < len(names):
#     print('Hello,',names[i]+'!')
#     i =i+ 1

# print([x if x % 2 == 0 else None for x in range(1, 11)])

# def char2num(s):
#      digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#      return digits[s]

# print(list(map(char2num, '13579')))

# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a

# f=Fib()
# print(f[10])

# print(range(6))

# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# import os
# print(os.path.abspath('.'))
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
# print([x for x in os.listdir('.') if os.path.isdir(x)])

# import json
# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))

# import os

# # 获取当前运行文件所在的目录路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

# # 列表生成式筛选该目录下的.py文件
# py_files = [file for file in os.listdir(current_dir) 
#             if os.path.isfile(os.path.join(current_dir, file)) and file.endswith('.py')]

# # 打印结果
# print(f"当前文件所在目录【{current_dir}】下的.py文件：")
# for f in py_files:
#     print(f)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# from tkinter import *

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()        

# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# # 导入socket库:
# import socket

# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接:
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# print('')
# # 把接收的数据写入文件:
# desktop_path = '/Users/ipromise/Desktop/sina.html'
# with open(desktop_path, 'wb') as f:
#     f.write(html)

# # import os
# # print(os.getcwd())  # 打印当前工作目录路径



# from email import encoders
# from email.header import Header#处理邮件头（发件人、收件人、主题）的编码（解决中文乱码问题）
# from email.mime.text import MIMEText#构造纯文本格式的邮件内容
# from email.mime.multipart import MIMEMultipart  # 新增：导入多部分邮件类
# from email.mime.base import MIMEBase            # 新增：导入附件基类
# from email.utils import parseaddr, formataddr#解析、格式化邮件地址（处理“名称 < 邮箱>”格式）

# import smtplib#实现 SMTP 协议，连接邮件服务器并发送邮件
 
# #`_format_addr()`函数用于格式化一个邮件地址	format——样式、版式   
# def _format_addr(s):
#     name, addr = parseaddr(s)#把“名称<邮箱>”拆分成name（名称）和addr（邮箱）
#     return formataddr((Header(name, 'utf-8').encode(), addr))
# 	#名称用UTF-8编码（支持中文名称）,formataddr()用于重新组合成标准的邮件地址格式

# #输入邮件信息
# from_addr = input('From: ')
# password = input('Password: ')#这里password不是邮箱密码,是授权码
# to_addr = input('To: ')#收件人邮箱,多个收件人用逗号分隔
# smtp_server = input('SMTP server: ')#发件人邮箱对应的服务商提供的服务器地址,形如smtp.qq.com

# # 邮件对象:
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# # 邮件正文是MIMEText:
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#     '<p><img src="cid:0"></p>' +
#     '</body></html>', 'html', 'utf-8'))

# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('/Users/ipromise/Desktop/测试图片.png', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIME15867Base('image', 'png', filename='test.png')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)

# #连接 SMTP 服务器并发送
# server = smtplib.SMTP_SSL(smtp_server, 465)#这里要改成465端口,smtplib用于连接SMTP服务器
# server.set_debuglevel(1)#开启调试模式，显示发送过程的日志
# server.login(from_addr, password)#用发件人邮箱和密码/授权码登录服务器
# server.sendmail(from_addr, [to_addr], msg.as_string())#发送邮件
# server.quit()#关闭连接

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)